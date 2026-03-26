
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None value
    maybe_none = Maybe(value=None, is_nothing=False)
    assert not maybe_none.is_nothing
    assert maybe_none.value is None
    
    # Test empty list
    maybe_empty_list = Maybe(value=[], is_nothing=False)
    assert not maybe_empty_list.is_nothing
    assert maybe_empty_list.value == []
    
    # Test boundary values
    maybe_zero = Maybe(value=0, is_nothing=False)
    assert not maybe_zero.is_nothing
    assert maybe_zero.value == 0
    
    maybe_one = Maybe(value=1, is_nothing=False)
    assert not maybe_one.is_nothing
    assert maybe_one.value == 1
    
    # Test empty Maybe (Nothing)
    maybe_nothing = Maybe(value=None, is_nothing=True)
    assert maybe_nothing.is_nothing
    with pytest.raises(AttributeError):
        assert maybe_nothing.value is None
