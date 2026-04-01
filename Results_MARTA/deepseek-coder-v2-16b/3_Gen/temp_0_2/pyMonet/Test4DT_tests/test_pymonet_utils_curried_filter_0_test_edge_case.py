
import pytest

def curried_filter(filterer, collection):
    return [item for item in collection if filterer(item)]

def test_edge_case():
    # Test with an empty list
    assert curried_filter(lambda x: True, []) == []
    
    # Test with None input
    with pytest.raises(TypeError):
        curried_filter(lambda x: True, None)
