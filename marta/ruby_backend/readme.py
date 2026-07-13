"""README analysis → per-method ``what_todo`` (item 7).

The Ruby counterpart to MARTA's ``DictionaryMessage`` + ``analyze_what_todo``:
the nearest README (walking up the directory tree, like ``find_readme``) is
distilled into a project overview, which — together with the method source —
drives a *requirement-perspective* summary ("what it is intended to do").
``summaries.generate_summary`` then merges that with the implementation-view
``done_what``.

The call-graph propagation of ``what_todo`` to callees defers with the graph.
"""
from __future__ import annotations

import os
from typing import Awaitable, Callable, Dict, Optional

AskFn = Callable[[str, str], Awaitable[str]]

README_NAMES = ("README.md", "README.markdown", "README.rdoc", "README")


def nearest_readme(file_path: str, abs_source: str) -> Optional[str]:
    """First README found walking up from the file's directory to abs_source."""
    abs_source = os.path.abspath(abs_source)
    d = os.path.dirname(os.path.abspath(file_path))
    while True:
        for name in README_NAMES:
            cand = os.path.join(d, name)
            if os.path.isfile(cand):
                return cand
        if os.path.abspath(d) == abs_source or os.path.dirname(d) == d:
            return None
        d = os.path.dirname(d)


_OVERVIEW_SYS = (
    "You are tasked with analyzing the contents of a README file and providing a "
    "clear, concise summary of what the project is about. Highlight the primary "
    "objectives and core functionality. Avoid excessive detail; aim for one or two "
    "short paragraphs conveying the project's purpose."
)


async def analyze_readme(ask: AskFn, readme_text: str) -> str:
    user = (
        "Please analyze the following README and summarize what the project aims "
        f"to do.\n{readme_text}"
    )
    return await ask(_OVERVIEW_SYS, user)


_WHAT_TODO_SYS_WITH_README = (
    "You are an AI assistant specialized in analyzing Ruby code. Examine the given "
    "method and generate a concise, clear summary that describes its purpose and "
    "usage. Consider the overall project objective for context, but focus on the "
    "method itself. Only output the summary content; do not include the source "
    "code, Ruby comments, or YARD tags."
)

_WHAT_TODO_SYS_PLAIN = (
    "You are an AI assistant that analyzes Ruby methods and provides a concise "
    "summary of their purpose and usage. Maintain clarity and precision while "
    "avoiding unnecessary detail. Only output the summary content; no source code, "
    "Ruby comments, or YARD tags."
)


async def analyze_what_todo(
    ask: AskFn, method_source: str, readme_overview: Optional[str]
) -> str:
    """Requirement-perspective summary of the method, informed by the README."""
    if readme_overview:
        sys_prompt = _WHAT_TODO_SYS_WITH_README
        user = (
            f"**Project Overview:**\n{readme_overview}\n\n"
            f"**Method Source Code:**\n```ruby\n{method_source}\n```"
        )
    else:
        sys_prompt = _WHAT_TODO_SYS_PLAIN
        user = (
            "Here is a Ruby method. Analyze its purpose and provide a summary of "
            f"what it does and how to use it.\n```ruby\n{method_source}\n```"
        )
    return await ask(sys_prompt, user)


class ReadmeOverviewCache:
    """Analyse each README once, reuse the overview across methods under it."""

    def __init__(self, abs_source: str):
        self.abs_source = abs_source
        self._by_path: Dict[str, str] = {}

    async def overview_for(self, ask: AskFn, file_path: str) -> Optional[str]:
        path = nearest_readme(file_path, self.abs_source)
        if path is None:
            return None
        if path not in self._by_path:
            with open(path, "r", encoding="utf-8") as f:
                self._by_path[path] = await analyze_readme(ask, f.read())
        return self._by_path[path]
