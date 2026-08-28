
import pytest
from pymonet.immutable_list import ImmutableList



def test_invalid_input():
    with pytest.raises(TypeError):
        ImmutableList().append()