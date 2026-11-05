"""Explicit evidence policies; no invented probabilities or calibrated defaults."""
from __future__ import annotations

import math
import os

POLICY = "ruby-evidence-v1"


def evidence_policy():
    graph = os.getenv("MARTA_GRAPH_CONTEXT", "all")
    if graph not in ("all", "supported_only"):
        raise ValueError("MARTA_GRAPH_CONTEXT must be all or supported_only")
    names = ("MARTA_JUDGE_MIN_SIMILARITY", "MARTA_JUDGE_MIN_MARGIN")
    values = [os.getenv(name) for name in names]
    if any(value is not None for value in values) and not all(value is not None for value in values):
        raise ValueError("Declare both judge similarity and margin thresholds, or neither")
    thresholds = [None, None]
    if values[0] is not None:
        try:
            thresholds = [float(value) for value in values]
        except ValueError as error:
            raise ValueError("Judge thresholds must be finite numbers") from error
        if (not all(math.isfinite(value) for value in thresholds)
                or not -1 <= thresholds[0] <= 1 or not 0 <= thresholds[1] <= 2):
            raise ValueError("Judge similarity must be within [-1,1] and margin within [0,2]")
    return {"policy": POLICY, "graph_context": graph,
            "judge_min_similarity": thresholds[0], "judge_min_margin": thresholds[1]}


def semantic_decision(candidates, scored, policy):
    """Require complete compatible evidence, a strict winner and explicit gates."""
    scores = []
    for hit in scored:
        try:
            value = float(hit.score)
        except (TypeError, ValueError):
            value = float("nan")
        scores.append({"class": hit.target.method.qualified_name,
                       "cosine": value if math.isfinite(value) else None})
    decision = {"structural_candidates": list(candidates), "scores": scores,
                "selected": None, "reason": None, "policy": policy}
    if len(candidates) < 2:
        decision["reason"] = "no_structural_candidates" if not candidates else "structural_unique_no_semantic_selection"
    elif {item["class"] for item in scores} != set(candidates) or len(scores) != len(candidates):
        decision["reason"] = "incomplete_scored_evidence"
    elif any(item["cosine"] is None for item in scores):
        decision["reason"] = "nonfinite_score"
    elif policy["judge_min_similarity"] is None:
        decision["reason"] = "no_threshold_policy_declared"
    else:
        ranked = sorted(scores, key=lambda item: (-item["cosine"], item["class"]))
        best, second = ranked[:2]
        margin = best["cosine"] - second["cosine"]
        decision["margin"] = margin
        if margin <= 0:
            decision["reason"] = "tie"
        elif best["cosine"] < policy["judge_min_similarity"]:
            decision["reason"] = "below_similarity_threshold"
        elif margin < policy["judge_min_margin"]:
            decision["reason"] = "below_margin_threshold"
        else:
            decision.update(selected=best["class"], reason="declared_thresholds_met")
    return decision
