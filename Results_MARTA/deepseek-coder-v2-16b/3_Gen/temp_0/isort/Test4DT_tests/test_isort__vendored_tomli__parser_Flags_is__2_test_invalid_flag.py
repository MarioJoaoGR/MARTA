
from typing import Dict, List, Union

import pytest

Key = List[str]

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def is_(self, key: Key, flag: int) -> bool:
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

@pytest.fixture
def flags():
    return Flags()

def test_invalid_flag(flags):
    # Test with an invalid key
    assert not flags.is_(["nonexistent"], Flags.EXPLICIT_NEST)
    
    # Test with a valid key but no flag set
    flags._flags = {"valid_key": {"flags": {}, "recursive_flags": {}}}
    assert not flags.is_(["valid_key"], Flags.EXPLICIT_NEST)
    
    # Test with an invalid flag value
    flags._flags = {"valid_key": {"flags": {Flags.FROZEN: True}, "recursive_flags": {}}}
    assert not flags.is_(["valid_key"], 999)  # Invalid flag value
