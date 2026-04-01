
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_input():
    with pytest.raises(ValueError):
        empty_list = ImmutableList()
        invalid_addition = empty_list + 'not an ImmutableList'
