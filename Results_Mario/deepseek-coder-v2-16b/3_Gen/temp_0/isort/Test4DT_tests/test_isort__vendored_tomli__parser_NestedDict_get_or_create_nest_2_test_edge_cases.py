
import pytest
from isort._vendored.tomli._parser import NestedDict

def test_get_or_create_nest():
    nd = NestedDict()
    
    # Test getting or creating a nested dictionary
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {}, "Expected an empty dictionary for new nest"
    
    # Modify the structure to check if it returns existing nested dictionary
    nd.dict['a'] = {'b': {}}
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {}, "Expected an empty dictionary for existing nest"
    
    # Test accessing elements in a list context
    nd.dict['x'] = [1, 2, 3]
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['x'], access_lists=False)
