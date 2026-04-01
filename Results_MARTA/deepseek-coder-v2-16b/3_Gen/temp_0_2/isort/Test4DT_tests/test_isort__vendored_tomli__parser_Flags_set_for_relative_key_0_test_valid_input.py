
import pytest
from typing import Dict, List

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def set_for_relative_key(self, head_key: List[str], rel_key: List[str], flag: int) -> None:
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

def test_valid_input():
    flags = Flags()
    head_key = ["a"]
    rel_key = ["b", "c"]
    
    # Test setting a valid flag for a relative key
    flags.set_for_relative_key(head_key, rel_key, Flags.EXPLICIT_NEST)
    assert flags._flags["a"]["nested"]["b"]["nested"]["c"]["flags"] == {Flags.EXPLICIT_NEST}
