
import pytest
from isort._vendored.tomli._parser import NestedDict

def test_valid_input():
    nd = NestedDict()
    
    # Test getting or creating a nested dictionary
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {}, "Expected an empty dictionary"
    
    # Modify the structure to check if it returns the existing nest
    nd.dict['a'] = {'b': {}}
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {}, "Expected an empty dictionary"
    
    # Test accessing elements in a list context
    nd.dict['x'] = [1, 2, 3]
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['x'], access_lists=False)
