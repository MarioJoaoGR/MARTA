
import pytest
from typing import Dict, Sequence

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def set(self, key: Sequence[str], flag: int, *, recursive: bool) -> None:  # noqa: A003
        """Sets a flag for a given key and determines whether the setting should be applied recursively.
        
        Parameters:
            key (Sequence[str]): A sequence of strings representing the namespace where the flag is to be set.
            flag (int): The flag value to be set, which can be one of FROZEN or EXPLICIT_NEST.
            recursive (bool): A boolean indicating whether the setting should apply recursively to nested namespaces.
            
        Returns:
            None
        
        Example:
            flags = Flags()
            flags.set(["a", "b", "c"], Flags.EXPLICIT_NEST, recursive=True)
            This sets the flag EXPLICIT_NEST in the namespace ["a", "b", "c"] and all its nested namespaces.
            
            flags.set(["x", "y", "z"], Flags.FROZEN, recursive=False)
            This sets the flag FROZEN in the namespace ["x", "y", "z"] but not in any of its nested namespaces.
        """
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                cont[k] = {"flags": set(), "recursive_flags": set(), "nested": {}}
            cont = cont[k]["nested"]
        if key[-1] not in cont:
            cont[key[-1]] = {"flags": set(), "recursive_flags": set(), "nested": {}}
        cont[key[-1]]["recursive_flags" if recursive else "flags"].add(flag)

def test_edge_case_none():
    flags = Flags()
    
    # Test setting a flag with None input for key, flag, and recursive
    with pytest.raises(TypeError):
        flags.set(None, None, recursive=None)
