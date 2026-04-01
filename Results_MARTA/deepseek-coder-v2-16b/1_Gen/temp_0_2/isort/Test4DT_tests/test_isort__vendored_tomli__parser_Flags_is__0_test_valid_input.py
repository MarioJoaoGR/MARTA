
import pytest
from typing import Dict, Sequence

Key = Sequence[str]

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

def test_valid_input():
    flags = Flags()
    # Adding a valid key and setting the flag
    flags._flags['some'] = {'nested': {}, 'flags': {Flags.EXPLICIT_NEST: True}, 'recursive_flags': {}}
    assert flags.is_(('some',), Flags.EXPLICIT_NEST) == True
    
    # Adding a valid key and setting the flag in nested structure
    flags._flags['some'] = {'nested': {}, 'flags': {}, 'recursive_flags': {Flags.EXPLICIT_NEST: True}}
    assert flags.is_(('some',), Flags.EXPLICIT_NEST) == True
    
    # Adding a valid key and setting the flag in nested structure with recursive flag
    flags._flags['some'] = {'nested': {}, 'flags': {Flags.EXPLICIT_NEST: True}, 'recursive_flags': {Flags.EXPLICIT_NEST: True}}
    assert flags.is_(('some',), Flags.EXPLICIT_NEST) == True
    
    # Adding an invalid key and checking the flag
    assert flags.is_(('invalid',), Flags.EXPLICIT_NEST) == False
