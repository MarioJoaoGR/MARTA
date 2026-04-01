
import pytest
from typing import Dict, List, Union

Key = List[str]

class Flags:
    """Flags that map to parsed keys/namespaces."""
    
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def unset_all(self, key: Key) -> None:
        """Unsets all flags in the nested dictionary corresponding to the given key.
        
        This function iterates through the keys of the provided `key` argument, traversing 
        the nested dictionary structure within `self._flags`. If a key is not found at any level, 
        it returns immediately without making any changes. Otherwise, it removes the last key in the sequence.
        
        Parameters:
            key (Key): A sequence of keys representing the path to the flags to be unset. The last key in this sequence will be removed if present.
        
        Returns:
            None
        
        Example:
            >>> flags = Flags()
            >>> flags._flags['a'] = {'nested': {}}
            >>> flags.unset_all(['a'])  # Removes the nested dictionary at 'a'
            
            If 'a' does not exist, no changes are made to `self._flags`.
        """
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return
            cont = cont[k]["nested"]
        cont.pop(key[-1], None)

def test_invalid_input():
    flags = Flags()
    with pytest.raises(TypeError):  # Expecting a TypeError for invalid input
        flags.unset_all(None)  # Passing None as the key argument, which should raise a TypeError
