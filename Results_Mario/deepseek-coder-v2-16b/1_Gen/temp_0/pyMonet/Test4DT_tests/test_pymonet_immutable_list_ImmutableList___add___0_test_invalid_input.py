
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_input():
    invalid_instance = 'InvalidType'
    with pytest.raises(ValueError):
        ImmutableList().__add__(invalid_instance)
