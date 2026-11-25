#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Write the folder that runs every recorded-run prompt against a local model on Windows. Standard library and Node.js.

    python3 tools/local_run_pack.py OUT [--model NAME] [--endpoint URL]

OUT receives the exact prompts the workflows send today (built by tools/n8n_replay_model.py from the
workflows' own Prepare nodes), `settings.json`, `run.ps1`, a `.cmd` to double-click and a short READ ME.
The person with the model runs the .cmd; `outputs/` then holds one file per prompt file, in the shape
tools/n8n_replay_model.py replays. The script asks once more, with the workflows' fixed instruction, when
an answer is not one JSON object, and records that second answer as `retry_content`.

The model sees the prompts only. Nothing here goes through n8n, and no customer data is involved:
every message is invented. The PowerShell script uses only what Windows PowerShell 5.1 has.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import dataset_pack as pack  # noqa: E402
import n8n_replay_model as replay  # noqa: E402

T1 = "01-whatsapp-customer-service"

RUN_PS1 = r'''# SAAEA local model run. Windows PowerShell 5.1 or newer. ASCII only: the Arabic text is read from the JSON files.
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$utf8 = New-Object System.Text.UTF8Encoding($false)
function ReadJson($path) { return ([System.IO.File]::ReadAllText($path, $utf8) | ConvertFrom-Json) }
function WriteJson($path, $value) { [System.IO.File]::WriteAllText($path, ($value | ConvertTo-Json -Depth 8), $utf8) }
$settings = ReadJson (Join-Path $here 'settings.json')

function Ask($messages) {
  $body = @{ model = $settings.model; temperature = 0; stream = $false; messages = $messages } | ConvertTo-Json -Depth 8
  $bytes = $utf8.GetBytes($body)
  $request = [System.Net.HttpWebRequest]::Create($settings.endpoint)
  $request.Method = 'POST'
  $request.Proxy = $null
  $request.ContentType = 'application/json; charset=utf-8'
  $request.Timeout = 900000
  $request.ReadWriteTimeout = 900000
  $stream = $request.GetRequestStream()
  $stream.Write($bytes, 0, $bytes.Length)
  $stream.Close()
  $response = $request.GetResponse()
  $reader = New-Object System.IO.StreamReader($response.GetResponseStream(), $utf8)
  $text = $reader.ReadToEnd()
  $reader.Close()
  $response.Close()
  return [string](($text | ConvertFrom-Json).choices[0].message.content)
}

function IsOneObject($text) {
  $t = ([string]$text).Trim()
  if (-not ($t.StartsWith('{') -and $t.EndsWith('}'))) { return $false }
  try { $null = $t | ConvertFrom-Json; return $true } catch { return $false }
}

try { $null = Ask @(@{ role = 'user'; content = 'ping' }) } catch {
  Write-Host ''
  Write-Host 'The model did not answer. Start Ollama, check the model name in settings.json, then run again.' -ForegroundColor Yellow
  Write-Host $_.Exception.Message
  exit 1
}

$outDir = Join-Path $here 'outputs'
if (-not (Test-Path $outDir)) { $null = New-Item -ItemType Directory -Path $outDir }
$files = Get-ChildItem (Join-Path $here 'prompts') -Filter '*.json' | Sort-Object Name
$total = 0
foreach ($file in $files) { $total += @(ReadJson $file.FullName).Count }
$done = 0
$started = Get-Date
foreach ($file in $files) {
  $name = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
  $target = Join-Path $outDir $file.Name
  $prompts = @(ReadJson $file.FullName)
  if (Test-Path $target) {
    $have = ReadJson $target
    if (@($have.outputs).Count -eq $prompts.Count) { $done += $prompts.Count; Write-Host "$name already done"; continue }
  }
  $outputs = New-Object System.Collections.ArrayList
  foreach ($p in $prompts) {
    $messages = @(@{ role = 'system'; content = [string]$p.system }, @{ role = 'user'; content = [string]$p.user })
    $watch = [System.Diagnostics.Stopwatch]::StartNew()
    $content = Ask $messages
    $item = [ordered]@{ id = $p.id; content = $content; seconds = [math]::Round($watch.Elapsed.TotalSeconds, 1) }
    if ($p.ref) { $item.ref = [string]$p.ref }
    if (-not (IsOneObject $content)) {
      $clip = $content
      if ($clip.Length -gt 2000) { $clip = $clip.Substring(0, 2000) }
      $again = $messages + @(@{ role = 'assistant'; content = $clip }, @{ role = 'user'; content = [string]$settings.retry_instruction })
      $watch = [System.Diagnostics.Stopwatch]::StartNew()
      $item.retry_content = Ask $again
      $item.retry_seconds = [math]::Round($watch.Elapsed.TotalSeconds, 1)
    }
    $null = $outputs.Add($item)
    $done += 1
    Write-Host ("{0}/{1}  {2} #{3}" -f $done, $total, $name, $p.id)
    WriteJson $target ([ordered]@{ workflow = $name; model = [string]$settings.model_label; date = (Get-Date -Format 'yyyy-MM-dd'); how = [string]$settings.how; outputs = $outputs.ToArray() })
  }
}
$minutes = [math]::Round(((Get-Date) - $started).TotalMinutes, 1)
WriteJson (Join-Path $outDir '_run.json') ([ordered]@{ prompts = $total; minutes = $minutes; finished = (Get-Date -Format 'yyyy-MM-dd HH:mm') })
Write-Host ''
Write-Host "Done: $total prompts in $minutes minutes. The answers are in the 'outputs' folder." -ForegroundColor Green
'''

RUN_CMD = '@echo off\r\ncd /d "%~dp0"\r\npowershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run.ps1"\r\necho.\r\npause\r\n'

READ_ME = """SAAEA local model test

1. Make sure Ollama is running (its icon is in the system tray).
2. Double-click "Run local model test.cmd".
3. Wait until it says Done. It prints one line per prompt. If it stops, run it again: it skips the files that are finished.
4. The answers are in the "outputs" folder.

It sends {count} prompts to the model named in settings.json, on this computer only. Every message is invented.
"""


def retry_instruction():
    """The fixed second-ask instruction, read from the workflows' own node so the run matches them."""
    with open(os.path.join(replay.WORKFLOWS, "src", "common", "check_model.js"), encoding="utf-8") as f:
        return re.search(r"\{ role: 'user', content: '([^']+)' \}", f.read()).group(1)


def prompt_files():
    """(file name, prompts) for every recorded-run file: templates, lab, the store's messages and failure cases, dialect cases."""
    for name in sorted(os.listdir(os.path.join(replay.WORKFLOWS, "src"))):
        if name == "common":
            continue
        workflow, cases = replay.template_inputs(name)
        bodies = [{k: v for k, v in case.items() if k not in ("expect", "_config", "_model_response")} for case in cases]
        yield name, replay.prompts(workflow, bodies, {})
        dialect = os.path.join(replay.WORKFLOWS, "src", name, "dialect-cases.json")
        if os.path.exists(dialect):
            cases = replay.read(dialect)
            items = cases["cases"] + cases["simulator_limits"]
            built = replay.prompts(workflow, [{k: c[k] for k in ("message", "account") if k in c} for c in items], {})
            yield name + ".dialect", [dict(p, ref=c["ref"]) for p, c in zip(built, items)]
    lab = [{"message": c["message"], "account": c["account"]} for c in replay.lab_cases()]
    yield "lab-order-agent", replay.prompts(replay.LAB, lab, replay.lab_overrides())
    config = replay.read(pack.path("template-1-config.json"))
    for name, source in (("dataset-85", "requests.json"), ("dataset-failures-30", "failure-requests.json")):
        requests = replay.read(pack.path(source))
        built = replay.prompts(os.path.join(replay.WORKFLOWS, T1 + ".n8n.json"), requests, config)
        yield name, [dict(p, ref=q["ref"]) for p, q in zip(built, requests)]


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 1
    out = argv[0]
    option = lambda flag, default: argv[argv.index(flag) + 1] if flag in argv else default
    model = option("--model", "qwen2.5:3b")
    endpoint = option("--endpoint", "http://localhost:11434/v1/chat/completions")
    commit = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "unknown"
    os.makedirs(os.path.join(out, "prompts"), exist_ok=True)
    count = 0
    for name, prompts in prompt_files():
        count += len(prompts)
        with open(os.path.join(out, "prompts", name + ".json"), "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=1)
    settings = {"model": model, "model_label": "%s (Ollama, local)" % model, "endpoint": endpoint, "retry_instruction": retry_instruction(),
                "how": "One separate call per prompt to %s with temperature 0; the model saw the prompt only. When an answer was not one JSON "
                       "object the script asked once more with the workflows' fixed instruction and recorded retry_content. Not sent through "
                       "n8n's HTTP node. Prompts built by tools/local_run_pack.py at commit %s." % (endpoint, commit)}
    with open(os.path.join(out, "settings.json"), "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=1)
    for name, text in (("run.ps1", RUN_PS1.replace("\n", "\r\n")), ("Run local model test.cmd", RUN_CMD), ("READ ME.txt", READ_ME.format(count=count).replace("\n", "\r\n"))):
        with open(os.path.join(out, name), "w", encoding="ascii", newline="") as f:
            f.write(text)
    print("%d prompts in %s" % (count, out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
