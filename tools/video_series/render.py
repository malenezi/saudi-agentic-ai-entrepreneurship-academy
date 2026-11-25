# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Step 3. Build each video's page, film it scene by scene with headless Chrome, join, and add sound.

    python3 render.py stills v1          key frames and an overflow check, before filming
    python3 render.py film v1 [scene..]  one encoded file per scene
    python3 render.py mux v1             join the scenes and add voice and music
"""
import sys, json, os, subprocess, asyncio
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import VIDEOS
from playwright.async_api import async_playwright
W = os.path.join(HERE, 'build')  # pages, fonts, logo, audio and video all live here
CHROME = os.environ.get('SAAEA_CHROME', '/usr/bin/google-chrome')
FPS = 30
ENC = ['-c:v', 'libx264', '-crf', '19', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', str(FPS)]
FONTS = ''.join(
    f'@font-face{{font-family:"{fam}";font-weight:{w};src:url({f}-{w}-normal.woff2)}}'
    for fam, f in (("Plex Ar", "ibm-plex-sans-arabic-arabic"), ("Plex", "ibm-plex-sans-latin")) for w in (400, 500, 600, 700))


def build(V):
    tl = json.load(open(f"{W}/{V['id']}_tl.json"))
    sc = ''
    for i, S in enumerate(V['scenes']):
        light = ' lightbg' if 'sc end' in S['html'] else ''
        extra = '<svg id="ewave" viewBox="0 0 1920 170" preserveAspectRatio="none"><path d="M0 120 C 500 10, 1150 190, 1920 50 L1920 170 L0 170Z" fill="#0B2545"/><path d="M0 96 C 520 0, 1150 170, 1920 30" fill="none" stroke="#35C9C3" stroke-width="5"/></svg>' if light else ''
        sc += f'<div class="scene{light}">{S["html"]}{extra}</div>'
    h = open(os.path.join(HERE, 'base.html'), encoding='utf-8').read().replace('/*FONTS*/', FONTS).replace('<!--SCENES-->', sc)
    h = h.replace('<!--TITLE-->', V['title']).replace('<!--NUM-->', V['num']).replace('/*TL*/', json.dumps(tl))
    open(f"{W}/{V['id']}.html", 'w', encoding='utf-8').write(h)
    return tl


async def page_for(pw, V):
    b = await pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox', '--force-device-scale-factor=1', '--font-render-hinting=none'])
    p = await b.new_page(viewport=dict(width=1920, height=1080))
    errs = []
    p.on('pageerror', lambda e: errs.append(str(e)))
    await p.goto(f"file://{W}/{V['id']}.html")
    await p.evaluate('window.ready')
    if errs:
        raise SystemExit('page error: ' + '; '.join(errs))
    return b, p


async def stills(V, tl, times):
    async with async_playwright() as pw:
        b, p = await page_for(pw, V)
        for t in times:
            await p.evaluate(f'render({t})')
            await p.screenshot(path=f"{W}/still_{V['id']}_{t:06.2f}.jpg", type='jpeg', quality=80)
        # overflow check at each scene's last moment
        for i, s in enumerate(tl['scenes']):
            await p.evaluate(f"render({s['end']-0.05})")
            bad = await p.evaluate("""(i)=>{const sc=document.querySelectorAll('.scene')[i];const out=[];
              sc.querySelectorAll('.sc *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&(r.left<20||r.right>1900||r.top<100||r.bottom>1075))out.push(e.className+':'+Math.round(r.left)+','+Math.round(r.top)+','+Math.round(r.right)+','+Math.round(r.bottom))});
              sc.querySelectorAll('.card,.node,.chip,.nb,.col').forEach(e=>{if(e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2)out.push('overflow '+e.className)});return out}""", i)
            if bad:
                print(V['id'], 'scene', i, bad[:6])
        await b.close()


async def film(V, tl, which):
    async with async_playwright() as pw:
        b, p = await page_for(pw, V)
        n = len(tl['scenes'])
        for i in which:
            f0 = 0 if i == 0 else round(tl['scenes'][i]['start'] * FPS)
            f1 = round(tl['dur'] * FPS) if i == n - 1 else round(tl['scenes'][i + 1]['start'] * FPS)
            tmp, dst = f"{W}/{V['id']}_s{i}.tmp.mp4", f"{W}/{V['id']}_s{i}.mp4"
            ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', str(FPS), '-i', '-', *ENC, tmp], stdin=subprocess.PIPE)
            for f in range(f0, f1):
                await p.evaluate(f'render({f / FPS})')
                ff.stdin.write(await p.screenshot(type='jpeg', quality=92))
            ff.stdin.close()
            if ff.wait() == 0:
                os.replace(tmp, dst)
                print(V['id'], 'scene', i, f1 - f0, 'frames', flush=True)
            else:
                raise SystemExit('ffmpeg failed')
        await b.close()


def mux(V, tl):
    n = len(tl['scenes'])
    open(f"{W}/{V['id']}_list.txt", 'w').write(''.join(f"file '{V['id']}_s{i}.mp4'\n" for i in range(n)))
    subprocess.check_call(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f"{W}/{V['id']}_list.txt", '-c', 'copy', f"{W}/{V['id']}_video.mp4"])
    d = tl['dur']
    # voice: gentle clean-up and level; music: quiet bed, ducked a little further under speech
    fc = (f"[1:a]aresample=48000,highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=140,loudnorm=I=-16:TP=-1.5:LRA=9,apad=whole_dur={d},asplit=2[v][vs];"
          f"[2:a]atrim=0:{d},volume=0.20,afade=t=in:d=1.5,afade=t=out:st={d - 2.5}:d=2.5[m];"
          f"[m][vs]sidechaincompress=threshold=0.03:ratio=3:attack=60:release=700[md];"
          f"[v][md]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.9[a]")
    subprocess.check_call(['ffmpeg', '-y', '-loglevel', 'error', '-i', f"{W}/{V['id']}_video.mp4", '-i', f"{W}/{V['id']}_voice.wav", '-i', f'{W}/music.wav',
                           '-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', str(d), '-movflags', '+faststart', f"{W}/{V['id']}_final.mp4"])
    print('muxed', V['id'])


if __name__ == '__main__':
    cmd, vid = sys.argv[1], sys.argv[2]
    V = next(v for v in VIDEOS if v['id'] == vid)
    tl = build(V)
    if cmd == 'stills':
        ts = [float(x) for x in sys.argv[3:]] or [round(s['end'] - 0.1, 2) for s in tl['scenes'][:-1]] + [tl['dur'] - 0.3]
        asyncio.run(stills(V, tl, ts))
    elif cmd == 'film':
        asyncio.run(film(V, tl, [int(x) for x in sys.argv[3:]] or range(len(tl['scenes']))))
    elif cmd == 'mux':
        mux(V, tl)
