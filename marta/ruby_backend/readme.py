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

import hashlib
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Awaitable, Callable, Dict, Optional

AskFn = Callable[[str, str], Awaitable[str]]

README_NAMES = ("README.md", "README.markdown", "README.rdoc", "README")


README_POLICY = "nearest-within-project-v1"


def _within(path: str, root: str) -> bool:
    try:
        return os.path.commonpath([path, root]) == root
    except ValueError:
        return False


def nearest_readme(file_path: str, abs_source: str, *, project_root: Optional[str] = None) -> Optional[str]:
    """Nearest README up to the project root, inclusive.

    Two-argument callers retain their supplied source directory as the boundary.
    Project orchestration explicitly supplies its separate project root. Paths
    are resolved so a symlink cannot accidentally import another project's docs.
    """
    root = os.path.realpath(project_root if project_root is not None else abs_source)
    current = os.path.dirname(os.path.realpath(file_path))
    if not _within(current, root):
        return None
    while True:
        for name in README_NAMES:
            candidate = os.path.join(current, name)
            resolved = os.path.realpath(candidate)
            if _within(resolved, root) and os.path.isfile(candidate):
                return resolved
        if current == root:
            return None
        current = os.path.dirname(current)


@dataclass(frozen=True)
class ReadmeDocument:
    path: str
    content: str
    sha256: str


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
    """One immutable README snapshot and overview per document per analysis.

    Prefetch with manifest_for before computing analysis validity. Subsequent
    prompts use those exact bytes even if documentation changes during the run.
    """

    def __init__(self, abs_source: str, *, project_root: Optional[str] = None):
        self.abs_source = abs_source
        self.project_root = os.path.realpath(project_root if project_root is not None else abs_source)
        self._by_path: Dict[str, str] = {}
        self._documents: Dict[str, ReadmeDocument] = {}
        self._by_file: Dict[str, Optional[ReadmeDocument]] = {}

    def document_for(self, file_path: str) -> Optional[ReadmeDocument]:
        file_path = os.path.realpath(file_path)
        if file_path not in self._by_file:
            path = nearest_readme(file_path, self.abs_source, project_root=self.project_root)
            document = None
            if path is not None:
                if path not in self._documents:
                    data = Path(path).read_bytes()
                    self._documents[path] = ReadmeDocument(
                        path, data.decode("utf-8"), hashlib.sha256(data).hexdigest())
                document = self._documents[path]
            self._by_file[file_path] = document
        return self._by_file[file_path]

    def manifest_for(self, files):
        manifest = {}
        for file_path in sorted(set(files)):
            document = self.document_for(file_path)
            manifest[os.path.relpath(os.path.realpath(file_path), self.project_root)] = (
                {"path": os.path.relpath(document.path, self.project_root), "sha256": document.sha256}
                if document is not None else None)
        return manifest

    async def overview_for(self, ask: AskFn, file_path: str) -> Optional[str]:
        document = self.document_for(file_path)
        if document is None:
            return None
        if document.path not in self._by_path:
            self._by_path[document.path] = await analyze_readme(ask, document.content)
        return self._by_path[document.path]
