"""Conservative, query-memoized return candidates from direct constructors.

These are possible normal-return instance types, never a runtime guarantee.
No LLM, annotation parsing, recursive propagation or execution of Ruby code.
"""
from collections import defaultdict
from dataclasses import dataclass

POLICY = "direct-constructor-return-v1"
STATE_POLICY = "constructor-state-v1"


@dataclass(frozen=True)
class ReturnHint:
    candidates: tuple = ()
    reason: str = "unknown"
    via: tuple = ()
    required_receiver: str | None = None


class ReturnTypeIndex:
    def __init__(self, methods, type_index):
        self.types = type_index
        self.definitions = defaultdict(list)
        for method in methods:
            self.definitions[method.qualified_name].append(method)
        self._cache = {}
        self._state = None

    def for_method(self, qualified_name):
        if qualified_name not in self._cache:
            self._cache[qualified_name] = self._infer(qualified_name)
        return self._cache[qualified_name]

    def _state_index(self):
        if self._state is None:
            self._state = _ConstructorStateIndex(self)
        return self._state

    def for_ivar(self, owner, name):
        return self._state_index().for_ivar(owner, name)

    def _infer(self, name):
        definitions = self.definitions.get(name, ())
        if not definitions:
            owner, separator, member = name.rpartition("#")
            if separator and member in self.types.attribute_methods.get(owner, set()):
                return self._state_index().for_getter(owner, member)
            return ReturnHint(reason="missing_definition")
        if len(definitions) != 1:
            return ReturnHint(reason="ambiguous_definition")
        method = definitions[0]
        if method.singleton and method.name == "new":
            return ReturnHint(reason="custom_constructor_method")
        if not method.singleton and method.name in self.types.attribute_methods.get(method.owner, set()):
            return ReturnHint(reason="generated_method_conflict")
        fact = getattr(method, "return_fact", None)
        if not fact:
            return ReturnHint(reason="missing_source_fact")
        if fact.get("policy") == STATE_POLICY and fact.get("kind") == "instance_ivar" and not method.singleton:
            return self.for_ivar(method.owner, fact.get("ivar"))
        if fact.get("policy") == POLICY and fact.get("kind") == "receiver_new" and method.singleton:
            # The receiver of an inherited factory can differ from its owner.
            hint = self._constructor_hint({"policy": POLICY, "kind": "constant_new",
                                           "constant": method.owner})
            if hint.candidates:
                return ReturnHint(hint.candidates, "receiver_constructor_candidate",
                                  required_receiver=method.owner)
            return hint
        return self._constructor_hint(fact)

    def _constructor_hint(self, fact):
        if not isinstance(fact, dict):
            return ReturnHint(reason="missing_constructor_candidate")
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


class _ConstructorStateIndex:
    """Lazy closed-owner state checks, never a claim of runtime immutability."""
    def __init__(self, returns):
        self.returns, self.types = returns, returns.types
        self._cache = {}
        self.blocked = None
        if not self.types.state_complete or any(
                not method.state_scanned for group in returns.definitions.values() for method in group):
            self.blocked = ReturnHint(reason="incomplete_state_metadata")
        elif self.types.state_opaque:
            self.blocked = ReturnHint(reason="opaque_project_state_effects")
        self.writes, self.children = {}, set()
        if self.blocked is not None:
            return  # Do not build unused tables for opaque/legacy projects.
        for group in returns.definitions.values():
            for method in group:
                if method.singleton:
                    continue  # Class-object ivars are not instance-object ivars.
                for variable, count in (method.state_effects or {}).get("writes", {}).items():
                    key = (method.owner, variable)
                    bucket = self.writes.setdefault(key, {})
                    bucket[method.qualified_name] = bucket.get(method.qualified_name, 0) + count
        for declarations in self.types.state_declarations.values():
            for declaration in declarations:
                self.children.update(self.types.resolve_candidates(declaration["superclass"]))

    def for_getter(self, owner, name):
        if self.blocked is not None:
            return self.blocked
        declarations = self.types.state_declarations.get(owner, ())
        readers = sum((d.get("facts") or {}).get("readers", []).count(name) for d in declarations)
        if readers != 1:
            return ReturnHint(reason="ambiguous_or_missing_generated_reader")
        return self.for_ivar(owner, "@" + name)

    def for_ivar(self, owner, name):
        if self.blocked is not None:
            return self.blocked
        key = (owner, name)
        if key not in self._cache:
            self._cache[key] = self._infer(owner, name)
        return self._cache[key]

    def _infer(self, owner, name):
        cls = self.types.classes.get(owner)
        if cls is None or cls.kind != "class" or not isinstance(name, str) or not name.startswith("@") or name.startswith("@@"):
            return ReturnHint(reason="unsupported_state_owner")
        declarations = self.types.state_declarations.get(owner, ())
        if not declarations or any(d["kind"] != "class" or d["superclass"] is not None
                                   or not (d.get("facts") or {}).get("closed_body") for d in declarations):
            return ReturnHint(reason="open_or_inherited_state_owner")
        if owner in self.children:
            return ReturnHint(reason="known_subclasses")
        if any(self.returns.definitions.get(owner + "." + api)
               for api in ("new", "allocate", "attr_reader", "attr_writer", "attr_accessor")):
            return ReturnHint(reason="custom_owner_construction_api")
        if any(name[1:] in d["facts"].get("writers", []) for d in declarations):
            return ReturnHint(reason="exposed_attribute_writer")
        initializer = owner + "#initialize"
        definitions = self.returns.definitions.get(initializer, ())
        if len(definitions) != 1:
            return ReturnHint(reason="ambiguous_or_missing_initializer")
        constructor = (definitions[0].state_effects or {}).get("constructor", {})
        if not constructor.get("closed"):
            return ReturnHint(reason="unsupported_constructor")
        if self.writes.get((owner, name)) != {initializer: 1}:
            return ReturnHint(reason="other_or_repeated_ivar_writes")
        assignments = constructor.get("assignments")
        if not isinstance(assignments, dict):
            return ReturnHint(reason="incomplete_constructor_metadata")
        fact = assignments.get(name)
        if isinstance(fact, dict) and not fact["constant"].startswith("::"):
            first = fact["constant"].split("::", 1)[0]
            scope = owner
            while scope:
                if any(first in (d.get("facts") or {}).get("constants", [])
                       for d in self.types.state_declarations.get(scope, ())):
                    return ReturnHint(reason="lexical_constant_assignment")
                scope = scope.rpartition("::")[0]
        hint = self.returns._constructor_hint(fact)
        if not hint.candidates:
            return hint
        return ReturnHint(hint.candidates, "constructor_ivar_candidate", (initializer,))
