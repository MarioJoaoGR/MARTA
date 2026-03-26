
from typing import Dict, Sequence

import pytest


class Flags:
    """Flags that map to parsed keys/namespaces."""
    
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def set_flag(self, key: Sequence[str], flag: int) -> None:
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                cont[k] = {"flags": set(), "recursive_flags": set(), "nested": {}}
            cont = cont[k]["nested"]
        cont[key[-1]] = {"flags": {flag}, "recursive_flags": set(), "nested": {}}

    def unset_all(self, key: Sequence[str]) -> None:
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return
            cont = cont[k]["nested"]
        cont.pop(key[-1], None)

    def set_for_relative_key(self, head_key: Sequence[str], rel_key: Sequence[str], flag: int) -> None:
        cont = self._flags
        for k in head_key:
            if k not in cont:
                cont[k] = {"flags": set(), "recursive_flags": set(), "nested": {}}
            cont = cont[k]["nested"]
        for k in rel_key:
            if k in cont:
                cont[k]["flags"].add(flag)
            else:
                cont[k] = {"flags": {flag}, "recursive_flags": set(), "nested": {}}
            cont = cont[k]["nested"]

    def is_(self, key: Sequence[str], flag: int) -> bool:
        if not key:
            return False  # document root has no flags
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return False
            inner_cont = cont[k]
            if flag in inner_cont["recursive_flags"]:
                return True
            cont = inner_cont["nested"]
        key_stem = key[-1]
        if key_stem in cont:
            cont = cont[key_stem]
            return flag in cont["flags"] or flag in cont["recursive_flags"]
        return False

# Test cases for Flags class
def test_initialization():
    flags = Flags()
    assert flags._flags == {}

def test_set_flag():
    flags = Flags()
    flags.set_flag(['namespace', 'subnamespace'], Flags.EXPLICIT_NEST)
    expected = {
        'namespace': {
            'nested': {
                'subnamespace': {'flags': {Flags.EXPLICIT_NEST}, 'recursive_flags': set(), 'nested': {}}
            }
        }
    }