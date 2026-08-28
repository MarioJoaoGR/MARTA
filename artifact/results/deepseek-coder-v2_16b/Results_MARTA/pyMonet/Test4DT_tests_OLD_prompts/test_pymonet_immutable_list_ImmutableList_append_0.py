
import pytest
from pymonet.immutable_list import ImmutableList


def test_invalid_input():
    with pytest.raises(TypeError):
        my_list = ImmutableList(is_empty=True)
        my_list.append()