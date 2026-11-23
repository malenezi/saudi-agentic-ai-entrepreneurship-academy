# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Run the Academy's twelve founder agents from the command line. Standard library only.

The agents stay defined in one place: the Markdown pages under
02-saudi-market-knowledge-framework/founder-agents/. This package reads those pages; it holds
no copy of a definition, a source page or a test conversation.

    registry   reads an agent's definition, the pages it reads and its three test conversations
    prompt     assembles what a model is given: the definition, the pages, the founder context
    models     a chat-completions client, and a scripted stand-in that is not a model
    checks     mechanical checks of a reply against the operating standard; flags for a person
    guard      looks for personal data and secrets in what the founder is about to send
    runner     runs a conversation or the three test conversations and writes the record
    recorded   reads the published recorded runs so that the same checks can be run on them
"""

__version__ = "0.1"
