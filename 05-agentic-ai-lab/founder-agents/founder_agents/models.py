# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The model step. One real client and one stand-in.

HttpModel      Any endpoint that follows the OpenAI chat-completions format, local or hosted.
               Configured with the same environment variables as the Course 2 lab:
                   SAAEA_MODEL_BASE_URL   for example http://localhost:11434/v1 for a local Ollama server
                   SAAEA_MODEL_NAME       the model name the endpoint expects
                   SAAEA_MODEL_API_KEY    optional for local runtimes; never put a key in a file
ScriptedModel  Returns replies it was handed, in order. It is NOT a language model. It exists so
               that the runner can be tested offline and so that a saved conversation can be
               replayed through the checks.

There is deliberately no keyword simulator here. A founder agent states regulatory and programme
information; a stand-in that produced such statements would be producing statements nobody checked.
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request


class ModelError(RuntimeError):
    """The model could not be reached or did not answer in the expected form."""


class HttpModel:
    def __init__(self, base_url=None, name=None, api_key=None, timeout=300, temperature=0):
        self.base_url = (base_url or os.environ.get("SAAEA_MODEL_BASE_URL", "")).rstrip("/")
        self.name = name or os.environ.get("SAAEA_MODEL_NAME", "")
        self.api_key = api_key or os.environ.get("SAAEA_MODEL_API_KEY", "")
        self.timeout, self.temperature, self.calls = timeout, temperature, 0
        if not self.base_url or not self.name:
            raise ModelError("Set SAAEA_MODEL_BASE_URL and SAAEA_MODEL_NAME. For a local Ollama server: "
                             "SAAEA_MODEL_BASE_URL=http://localhost:11434/v1 and SAAEA_MODEL_NAME=<a model you pulled>. "
                             "To use an assistant you already have, run the `prompt` command and paste its output.")

    @property
    def host(self):
        """Where the conversation is sent. Shown to the founder before the first message, and kept in the record."""
        return urllib.parse.urlsplit(self.base_url).netloc

    @property
    def is_local(self):
        return urllib.parse.urlsplit(self.base_url).hostname in ("localhost", "127.0.0.1", "::1")

    def reply(self, system, turns):
        """`turns` is the conversation so far: [{"role": "user"|"assistant", "content": str}, ...]."""
        self.calls += 1
        body = json.dumps({"model": self.name, "temperature": self.temperature,
                           "messages": [{"role": "system", "content": system}] + list(turns)}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = "Bearer " + self.api_key
        request = urllib.request.Request(self.base_url + "/chat/completions", data=body, headers=headers)
        # A local runtime is reached directly: a proxy set for the rest of the machine cannot reach localhost.
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({})) if self.is_local else urllib.request.build_opener()
        try:
            with opener.open(request, timeout=self.timeout) as response:
                content = json.load(response)["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as error:
            raise ModelError("The endpoint answered %d %s." % (error.code, error.reason))
        except (urllib.error.URLError, OSError) as error:
            raise ModelError("Could not reach %s: %s" % (self.host, getattr(error, "reason", error)))
        except (KeyError, IndexError, TypeError, ValueError):
            raise ModelError("The endpoint's answer is not in the chat-completions format.")
        if not isinstance(content, str) or not content.strip():
            raise ModelError("The model returned an empty reply.")
        return content


class ScriptedModel:
    """Hands back fixed replies in order. Not a language model."""

    host, is_local = "scripted (not a model)", True

    def __init__(self, replies, name="scripted"):
        self.replies, self.name, self.calls = list(replies), name, 0

    def reply(self, system, turns):
        if self.calls >= len(self.replies):
            raise ModelError("The script has %d replies and a further one was asked for." % len(self.replies))
        self.calls += 1
        return self.replies[self.calls - 1]
