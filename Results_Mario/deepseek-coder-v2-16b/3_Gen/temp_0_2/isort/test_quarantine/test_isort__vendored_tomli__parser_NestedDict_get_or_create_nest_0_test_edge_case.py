
import pytest
from unittest.mock import patch
from io import BytesIO
from tomli_w import TOMLWriter

class NestedDict:
    def __init__(self):
        self.dict = {}

    def get_or_create_nest(self, key, *, access_lists=True):
        cont = self.dict
        for k in key:
            if k not in cont:
                cont[k] = {}
            cont = cont[k]
            if access_lists and isinstance(cont, list):
                cont = cont[-1]
            if not isinstance(cont, dict):
                raise KeyError("There is no nest behind this key")
        return cont

# Test case for get_or_create_nest method
def test_get_or_create_nest():
    nd = NestedDict()
    
    # Create a nested structure
    nd.dict['a'] = {}
    nd.dict['a']['b'] = {'c': {}}
    
    # Test accessing an existing nest
    assert nd.get_or_create_nest(['a', 'b', 'c']) == {}
    
    # Test creating a new nest
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['a', 'x'])
    
    # Test accessing a list when access_lists is False
    nd.dict['a']['b'] = []
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['a', 'b'], access_lists=False)
    
    # Test creating a nest and ensuring it's a dictionary
    new_nest = nd.get_or_create_nest(['a', 'new'])
    assert isinstance(new_nest, dict)
    assert new_nest == {}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_edge_case
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_edge_case.py:5:0: E0401: Unable to import 'tomli_w' (import-error)


"""