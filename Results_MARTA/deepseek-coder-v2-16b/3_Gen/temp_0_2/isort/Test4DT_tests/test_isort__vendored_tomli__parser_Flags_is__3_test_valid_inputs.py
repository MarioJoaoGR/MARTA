
import pytest
from typing import Dict, Sequence

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def is_(self, key: Sequence[str], flag: int) -> bool:
        """
        Checks if a given flag is set for a specific key in the namespace.
        
        Parameters:
            key (Sequence[str]): A sequence representing the path to the key in the namespace.
            flag (int): The flag to check against the specified key.
            
        Returns:
            bool: True if the flag is set for the given key, otherwise False.
        """
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

def test_valid_inputs():
    flags = Flags()
    
    # Test with a valid key and flag that should be set
    assert not flags.is_(['key1'], Flags.FROZEN)  # Initially, no flags are set
    flags._flags['key1'] = {'flags': {Flags.EXPLICIT_NEST: True}, 'recursive_flags': {}, 'nested': {}}
    assert flags.is_(['key1'], Flags.EXPLICIT_NEST)  # Now the flag should be set
    
    # Test with a valid key and an invalid flag
    assert not flags.is_(['key1'], Flags.FROZEN)  # The flag is for EXPLICIT_NEST, not FROZEN
    
    # Test with a non-existent key
    assert not flags.is_(['non_existent_key'], Flags.EXPLICIT_NEST)  # No such key exists
