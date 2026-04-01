
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None case
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing is True
    with pytest.raises(AttributeError):
        assert maybe_none.value is None
