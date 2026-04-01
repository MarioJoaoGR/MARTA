
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    # Test None value
    maybe_none = Maybe(value=None, is_nothing=False)
    assert maybe_none.is_nothing == False
    assert maybe_none.value is None
    
    # Test empty value
    maybe_empty = Maybe(value="", is_nothing=True)
    assert maybe_empty.is_nothing == True
    with pytest.raises(AttributeError):
        assert maybe_empty.value == ""
