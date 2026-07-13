"""Two-perspective summary pipeline for the Ruby backend (item 3).

Faithful adaptation of MARTA's ``analyze_done_what`` / ``generate_summary``:

* ``done_what`` — "what the method does", from its source. When call-graph edges
  are available the called methods' summaries are folded in (the enrichment path
  MARTA gets from PyCG); until then it is source-only, exactly like MARTA's
  no-call-graph branch.
* ``summary`` — merges ``done_what`` with ``what_todo`` (the requirement view,
  from READMEs — arrives with DictionaryMessage). With no ``what_todo`` yet the
  merge is skipped and ``done_what`` stands in, saving a call.

Language-obligatory change: Ruby has no docstrings, so prompts ask for a concise
*summary* (kept internal, for RAG/context), never emitted as ``#``/YARD comments
into generated code (decision §4.7).
"""
from __future__ import annotations

from typing import Awaitable, Callable, List, Optional

AskFn = Callable[[str, str], Awaitable[str]]


_DONE_WHAT_SYS_PLAIN = (
    "You are a helpful assistant designed to analyze Ruby methods. "
    "Based on the provided source code of a method, your task is to generate a "
    "clear and concise summary of the given method. The summary should describe "
    "what the method does, what parameters it accepts, highlighting the role of "
    "each parameter and how changes to their values affect the method's execution, "
    "what it returns, and how to use the method effectively. Let's think step by "
    "step, only output the summary content. Do not include the source code or any "
    "extra explanations. Do NOT output Ruby comments or YARD tags."
)

_DONE_WHAT_SYS_WITH_CALLS = (
    "You are a helpful assistant designed to analyze Ruby methods. "
    "Based on the provided source code of a method and the summaries of the other "
    "methods it calls, your task is to generate a clear and concise summary of the "
    "given method. The summary should describe what the method does, what "
    "parameters it accepts, highlighting the role of each parameter and how changes "
    "to their values affect the method's execution, what it returns, and how to use "
    "the method effectively. Let's think step by step, only output the summary "
    "content. Do not include the source code or any extra explanations. Do NOT "
    "output Ruby comments or YARD tags."
)


async def analyze_done_what(
    ask: AskFn,
    method_source: str,
    called_summaries: Optional[List[str]] = None,
) -> str:
    """"What the method does", from its source (+ called-method summaries if a
    call graph provides them)."""
    call_message = ""
    if called_summaries:
        call_message = "\n".join(called_summaries)
        sys_prompt = _DONE_WHAT_SYS_WITH_CALLS
    else:
        sys_prompt = _DONE_WHAT_SYS_PLAIN
    user_prompt = (
        "Here is the source code of a Ruby method. Please analyze this and "
        "generate an appropriate summary for the provided method. Be sure to "
        "explain what the method does and how to use it.\n\n"
        f"source code: \n{method_source}\n\n methods it calls: \n{call_message}"
    )
    return await ask(sys_prompt, user_prompt)


_SUMMARY_SYS = (
    "You are an AI assistant skilled in analyzing and summarizing Ruby methods. "
    "Your task is to integrate two perspectives — one describing what the method "
    "does (implementation) and one describing what it is intended to do "
    "(requirement) — along with the source code, into a final, well-structured "
    "summary. Preserve and merge the key information from both, describe how to "
    "use the method (purpose, parameters, return value), and use clear, precise "
    "language. Only output the summary content; do not include the source code, "
    "Ruby comments, or YARD tags."
)


async def generate_summary(
    ask: AskFn,
    method_source: str,
    done_what: str,
    what_todo: Optional[str] = None,
) -> str:
    """Merge the two perspectives into the final summary. With no ``what_todo``
    the merge adds nothing, so ``done_what`` is returned as-is."""
    if not what_todo:
        return done_what
    user_prompt = (
        "Here is a Ruby method along with two summaries from different "
        "perspectives:\n\n"
        f"### Method Source Code:\n```ruby\n{method_source}\n```\n\n"
        f'### "What it does" summary:\n{done_what}\n\n'
        f'### "What it is intended to do" summary:\n{what_todo}\n'
    )
    return await ask(_SUMMARY_SYS, user_prompt)
