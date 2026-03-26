
import pytest
from typing import Dict, List

class Flags:
    """Flags that map to parsed keys/namespaces."""
    
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def unset_all(self, key: List[str]) -> None:
        """Unsets all flags in the nested dictionary corresponding to the given key.
        
        Parameters:
            key (List[str]): A sequence of keys representing the path to the flag or namespace you want to unset. The last key in the sequence corresponds to the specific flag or namespace to be removed.
            
        Returns:
            None
            
        Example:
            flags = Flags()
            flags._flags["a"] = {"nested": {}}
            flags._flags["a"]["nested"]["b"] = 1
            flags.unset_all(["a", "b"])  # This will remove the flag or namespace at key ["a", "b"]
        """
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return
            cont = cont[k]["nested"]
        cont.pop(key[-1], None)

def test_valid_input():
    flags = Flags()
    flags._flags["a"] = {"nested": {}}
    flags._flags["a"]["nested"]["b"] = 1
    
    # Test that the flag is unset correctly
    flags.unset_all(["a", "b"])
    assert "b" not in flags._flags["a"]["nested"]

    # Test that unsetting a non-existent key does nothing
    flags.unset_all(["a", "c"])
    assert "c" not in flags._flags["a"]["nested"]
