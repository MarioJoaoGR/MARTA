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

from .prompt_budget import OptionalPart, PromptBudget

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
    "method. Graph evidence labelled inferred, duck, fallback, ambiguous or legacy "
    "denotes possible relationships, not guaranteed runtime calls. Preserve that uncertainty. "
    "The summary should describe what the method does, what "
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
    *, budget: Optional[PromptBudget] = None, focal_source: Optional[str] = None,
) -> str:
    """"What the method does", from its source (+ called-method summaries if a
    call graph provides them)."""
    budget = budget or PromptBudget.from_ask(ask)
    sys_prompt = _DONE_WHAT_SYS_WITH_CALLS if called_summaries else _DONE_WHAT_SYS_PLAIN
    def render(values):
        call_message = "\n".join(values["callees"])
        return ("Here is the source code of a Ruby method. Please analyze this and "
                "generate an appropriate summary for the provided method. Be sure to "
                "explain what the method does and how to use it.\n\n"
                f"source code: \n{values['source_context']}\n\n methods it calls: \n{call_message}")
    user = budget.render(sys_prompt, render, [OptionalPart("callees", called_summaries or [], []),
        OptionalPart("source_context", method_source, focal_source or method_source, compact=False)])
    return await ask(sys_prompt, user)


_CLASS_SYS = (
    "You are a helpful assistant that analyzes Ruby classes. Based on the "
    "provided class source, generate a clear and concise summary describing the "
    "class's purpose, its main responsibilities, how to construct it, and how to "
    "use its methods when supported by the evidence. The input can be a partial "
    "static evidence view, not a complete executable class. Parser facts and "
    "generated implementation descriptions are labelled separately. Descriptions "
    "are source-based hypotheses, not verified runtime contracts. Do not invent "
    "defaults, visibility, return types, inherited behavior or a winning definition "
    "when declarations reopen or conflict. Treat omitted evidence as unknown. "
    "Only output the summary content; no source code, "
    "Ruby comments, or YARD tags."
)


async def analyze_class(ask: AskFn, class_source: str, *, budget: Optional[PromptBudget] = None,
                        class_core: Optional[str] = None,
                        class_evidence: Optional[List[str]] = None) -> str:
    """Summarize complete evidence records; retain the legacy raw-source API."""
    budget = budget or PromptBudget.from_ask(ask)
    if class_evidence is not None:
        user = budget.render(_CLASS_SYS, lambda values:
            f"Summarize this class from the supplied evidence.\n\n{class_source}\n\n"
            f"Evidence records submitted: {len(values['evidence'])}/{len(class_evidence)} prepared. "
            "Any further omitted records remain unknown.\n\n" + "\n\n".join(values["evidence"]),
            [OptionalPart("evidence", class_evidence, [])])
    else:
        user = budget.render(_CLASS_SYS, lambda values:
            "Here is the source code of a Ruby class. Summarize what it is for and "
            f"how to use it.\n```ruby\n{values['class_context']}\n```",
            [OptionalPart("class_context", class_source, class_core or class_source, compact=False)])
    return await ask(_CLASS_SYS, user)


_WHAT_TODO_FROM_CALLER_SYS = (
    "You are a Ruby code analysis assistant. Your task is to analyze a method "
    "call and produce a precise summary describing: the purpose of the called "
    "method, and the semantic roles and likely types of its parameters, inferred "
    "from the call context and the caller's intent — not just their names. Only "
    "output the summary content; no source code, Ruby comments, or YARD tags. "
    "A labelled best-effort graph relationship is evidence of a possible caller, "
    "not a runtime guarantee; do not turn that uncertainty into a requirement."
)


async def analyze_what_todo_from_caller(
    ask: AskFn,
    method_qn: str,
    method_source: str,
    caller_qn: str,
    caller_what_todo: str,
    *, budget: Optional[PromptBudget] = None, focal_source: Optional[str] = None,
    relationship: str = "",
) -> str:
    """Requirement view of a *called* method, propagated from its caller — the
    Ruby analogue of the callee branch of ``analyze_what_todo`` (which walks the
    PyCG edges). Roots get the README-based view; callees get this one."""
    budget = budget or PromptBudget.from_ask(ask)
    user = budget.render(_WHAT_TODO_FROM_CALLER_SYS, lambda values:
        f"Identify the purpose of the called method {method_qn} and explain how "
        f"to use it.\n\n" + (f"Graph relationship: {relationship}\n\n" if relationship else "") +
        f"Intent of the caller {caller_qn}:\n{values['caller_intent']}\n\n"
        f"Called method source:\n```ruby\n{values['source_context']}\n```",
        [OptionalPart("caller_intent", caller_what_todo, caller_what_todo[:128]),
         OptionalPart("source_context", method_source, focal_source or method_source, compact=False)])
    return await ask(_WHAT_TODO_FROM_CALLER_SYS, user)


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
    *, budget: Optional[PromptBudget] = None, focal_source: Optional[str] = None,
) -> str:
    """Merge the two perspectives into the final summary. With no ``what_todo``
    the merge adds nothing, so ``done_what`` is returned as-is."""
    if not what_todo:
        return done_what
    budget = budget or PromptBudget.from_ask(ask)
    user = budget.render(_SUMMARY_SYS, lambda values:
        "Here is a Ruby method along with two summaries from different "
        "perspectives:\n\n"
        f"### Method Source Code:\n```ruby\n{values['source_context']}\n```\n\n"
        f'### "What it does" summary:\n{values["done_what"]}\n\n'
        f'### "What it is intended to do" summary:\n{values["what_todo"]}\n',
        [OptionalPart("done_what", done_what, done_what[:128]),
         OptionalPart("what_todo", what_todo, what_todo[:128]),
         OptionalPart("source_context", method_source, focal_source or method_source, compact=False)])
    return await ask(_SUMMARY_SYS, user)
