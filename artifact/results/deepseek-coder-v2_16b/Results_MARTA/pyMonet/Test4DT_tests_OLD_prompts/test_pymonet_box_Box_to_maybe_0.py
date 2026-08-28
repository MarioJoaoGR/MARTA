
import pytest
from pymonet.box import Box


def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_validation()