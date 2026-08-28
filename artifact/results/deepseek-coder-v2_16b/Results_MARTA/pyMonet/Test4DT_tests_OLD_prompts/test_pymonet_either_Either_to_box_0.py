
import pytest
from pymonet.either import Either, Left, Right
from pymonet.box import Box


def test_invalid_input():
    with pytest.raises(TypeError):
        Either().to_box()