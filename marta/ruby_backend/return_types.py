"""Conservative, query-memoized return candidates from direct constructors.

These are possible normal-return instance types, never a runtime guarantee.
No LLM, annotation parsing, recursive propagation or execution of Ruby code.
"""
from collections import defaultdict
from dataclasses import dataclass

POLICY = "direct-constructor-return-v1"


@dataclass(frozen=True)
class ReturnHint:
    candidates: tuple = ()
    reason: str = "unknown"


class ReturnTypeIndex:
    def __init__(self, methods, type_index):
        self.types = type_index
        self.definitions = defaultdict(list)
        for method in methods:
            self.definitions[method.qualified_name].append(method)
        self._cache = {}

    def for_method(self, qualified_name):
        if qualified_name not in self._cache:
            self._cache[qualified_name] = self._infer(qualified_name)
        return self._cache[qualified_name]

    def _infer(self, name):
        definitions = self.definitions.get(name, ())
        if len(definitions) != 1:
            return ReturnHint(reason="ambiguous_definition" if definitions else "missing_definition")
        method = definitions[0]
        if method.singleton and method.name == "new":
            return ReturnHint(reason="custom_constructor_method")
        fact = getattr(method, "return_fact", None)
        if not fact:
            return ReturnHint(reason="missing_source_fact")
        if (fact.get("kind") != "constant_new" or fact.get("policy") != POLICY
                or not isinstance(fact.get("constant"), str)):
            return ReturnHint(reason="unsupported_source_fact")
        constant = fact["constant"]
        candidates = self.types.resolve_candidates(constant)
        if len(candidates) != 1:
            return ReturnHint(reason="ambiguous_project_constant" if candidates else "unknown_project_constant")
        candidate = candidates[0]
        if constant.removeprefix("::") != candidate:
            return ReturnHint(reason="non_exact_constant_lookup")
        cls = self.types.classes[candidate]
        if cls.kind != "class":
            return ReturnHint(reason="not_project_class")
        # Known custom new, including a project superclass, invalidates the
        # default-constructor hypothesis. Unknown runtime patches remain a limit.
        for ancestor in self.types.ancestors(candidate):
            if self.definitions.get(ancestor + ".new"):
                return ReturnHint(reason="custom_new")
            ancestor_cls = self.types.classes[ancestor]
            for extension in ancestor_cls.extends:
                for module in self.types.resolve_candidates(extension):
                    if any("new" in self.types.own_methods.get(provider, set())
                           for provider in self.types.ancestors(module)):
                        return ReturnHint(reason="custom_new_extension")
        return ReturnHint((candidate,), "direct_constructor_candidate")
