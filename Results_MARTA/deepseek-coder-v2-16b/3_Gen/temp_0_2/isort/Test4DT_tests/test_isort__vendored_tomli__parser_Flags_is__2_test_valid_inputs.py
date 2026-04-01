
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
        """
        Checks if a given flag is set for a specific key in the namespace.
        
        Parameters:
            key (Key): A sequence representing the path to the key in the namespace.
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
    
    # Test with a valid key and flag
    assert flags.is_(['key1'], Flags.EXPLICIT_NEST) == False
    
    # Set the flag for 'key1'
    flags._flags['key1'] = {'flags': {}, 'recursive_flags': {Flags.EXPLICIT_NEST}}
    assert flags.is_(['key1'], Flags.EXPLICIT_NEST) == True
    
    # Test with an invalid flag for the same key
    assert flags.is_(['key1'], Flags.FROZEN) == False
    
    # Set another valid flag for 'key2'
    flags._flags['key2'] = {'flags': {Flags.FROZEN}, 'recursive_flags': {}}
    assert flags.is_(['key2'], Flags.FROZEN) == True
