
from typing import Any, Dict, List, Union

import pytest


class NestedDict:
    """
    A class to handle nested dictionaries in Python.
    
    This class provides methods for creating and manipulating nested dictionaries. It can be used to parse TOML documents or any other data structured as a nested dictionary.
    
    Attributes:
        dict (dict): A nested dictionary containing the parsed content.
    
    Examples:
        >>> nd = NestedDict()
        >>> nd.set_value('a', 'b', 'c', 1)
        >>> print(nd.get_value('a', 'b', 'c'))
        1
        >>> nd.delete_key('a', 'b')
        >>> print(nd.get_value('a', 'b', 'c'))
        KeyError: 'c'
    
    """
    def __init__(self) -> None:
        # The parsed content of the TOML document
        self.dict: Dict[str, Any] = {}

    def get_or_create_nest(
        self,
        key: List[str],
        *,
        access_lists: bool = True,
    ) -> dict:
        cont: Any = self.dict
        for k in key:
            if k not in cont:
                cont[k] = {}
            cont = cont[k]
            if access_lists and isinstance(cont, list):
                cont = cont[-1]
            if not isinstance(cont, dict):
                raise KeyError("There is no nest behind this key")
        return cont

def test_valid_inputs():
    nd = NestedDict()
    
    # Test creating a new nested structure
    assert nd.get_or_create_nest(['a', 'b', 'c']) == {}
    assert nd.dict == {'a': {'b': {'c': {}}}}
    
    # Test accessing an existing nested structure
    nd.dict['a'] = {'b': {}}
    assert nd.get_or_create_nest(['a', 'b', 'c']) == {}
    
    # Test accessing a list element if access_lists is False
    nd.dict['x'] = [1, 2, 3]
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['x'], access_lists=False)
