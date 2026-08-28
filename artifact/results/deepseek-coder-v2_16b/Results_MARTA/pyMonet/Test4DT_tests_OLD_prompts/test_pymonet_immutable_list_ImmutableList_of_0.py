
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_inputs():
    with pytest.raises(TypeError):
        my_list = ImmutableList.of()
