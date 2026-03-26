
import pytest
from typing import Dict, List, Union

Key = List[str]

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def set(self, key: Key, flag: int, *, recursive: bool) -> None:  # noqa: A003
        """Sets a flag for a given key and determines whether the setting should be applied recursively.
        
        Parameters:
            key (Key): A sequence of keys representing the namespace where the flag is to be set.
            flag (int): The flag value to be set, which can be one of FROZEN or EXPLICIT_NEST.
            recursive (bool): A boolean indicating whether the setting should apply recursively to nested namespaces.
            
        Returns:
            None
        
        Example:
            flags = Flags()
            flags.set("a.b.c", Flags.EXPLICIT_NEST, recursive=True)
            This sets the flag EXPLICIT_NEST in the namespace "a.b.c" and all its nested namespaces.
            
            flags.set("x.y.z", Flags.FROZEN, recursive=False)
            This sets the flag FROZEN in the namespace "x.y.z" but not in any of its nested namespaces.
        """
        cont = self._flags
        key_parent, key_stem = key[:-1], key[-1]
        for k in key_parent:
            if k not in cont:
                cont[k] = {"flags": set(), "recursive_flags": set(), "nested": {}}
            cont = cont[k]["nested"]
        if key_stem not in cont:
            cont[key_stem] = {"flags": set(), "recursive_flags": set(), "nested": {}}
        cont[key_stem]["recursive_flags" if recursive else "flags"].add(flag)

def test_valid_input():
    flags = Flags()
    key = ["a", "b", "c"]
    
    # Test setting flag recursively to True
    flags.set(key, Flags.EXPLICIT_NEST, recursive=True)
    assert flags._flags["a"]["nested"]["b"]["nested"]["c"]["recursive_flags"] == {Flags.EXPLICIT_NEST}
    
    # Test setting flag recursively to False
    flags = Flags()  # Reset flags for the next test
    flags.set(key, Flags.EXPLICIT_NEST, recursive=False)
    assert flags._flags["a"]["nested"]["b"]["nested"]["c"]["flags"] == {Flags.EXPLICIT_NEST}
    
    # Test setting flag recursively to True with a new key
    flags = Flags()  # Reset flags for the next test
    flags.set(["new", "key"], Flags.FROZEN, recursive=True)
    assert flags._flags["new"]["nested"]["key"]["recursive_flags"] == {Flags.FROZEN}
    
    # Test setting flag recursively to False with a new key
    flags = Flags()  # Reset flags for the next test
    flags.set(["another", "key"], Flags.FROZEN, recursive=False)
    assert flags._flags["another"]["nested"]["key"]["flags"] == {Flags.FROZEN}
