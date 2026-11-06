"""A bounded, deterministic schedule for single-caller intent synthesis.

No model calls here. Prefer minimum root distance, then supported edge, then
caller name within the previous layer. This is a policy, not semantic optimality.
"""
from dataclasses import dataclass

POLICY = "intent-root-layers-v1"


@dataclass(frozen=True)
class IntentStep:
    callee: str
    caller: str
    depth: int


@dataclass(frozen=True)
class IntentSchedule:
    roots: tuple
    layers: tuple
    fallback: tuple


def plan_intent_flow(names, graph=None, *, supported_only=False):
    """Inspect each eligible adjacency once; each reachable method gets one step.

    Names must already exclude ambiguous definitions. Edges to omitted names do
    not turn a supplied method into a non-root. Unreachable cycles use fallback.
    """
    nodes = set(names)
    children = {}
    roots = []
    for callee in sorted(nodes):
        callers = set(graph.callers(callee, supported_only=supported_only)) & nodes if graph else set()
        if not callers:
            roots.append(callee)
        for caller in callers:
            children.setdefault(caller, []).append(callee)
    frontier = tuple(roots)
    seen = set(roots)
    layers = []
    depth = 0
    while frontier:
        candidates = {}
        for caller in frontier:
            for callee in children.get(caller, ()):
                if callee not in seen:
                    rank = (not graph.has_supported(caller, callee), caller)
                    if callee not in candidates or rank < candidates[callee]:
                        candidates[callee] = rank
        if not candidates:
            break
        depth += 1
        frontier = tuple(sorted(candidates))
        layers.append(tuple(IntentStep(callee, candidates[callee][1], depth) for callee in frontier))
        seen.update(frontier)
    return IntentSchedule(tuple(roots), tuple(layers), tuple(sorted(nodes - seen)))
