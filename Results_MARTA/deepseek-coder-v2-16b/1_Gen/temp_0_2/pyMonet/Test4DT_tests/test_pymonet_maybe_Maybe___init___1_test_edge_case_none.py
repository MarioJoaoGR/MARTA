
import pytest
from pymonet.maybe import Maybe

def test_edge_case_none():
    nothing = Maybe(value=None, is_nothing=True)
    assert nothing.is_nothing == True
    with pytest.raises(AttributeError):
        print(nothing.value)  # This should raise an AttributeError because the value should not be accessible when is_nothing is True
