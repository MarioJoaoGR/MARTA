
import pytest
from pymonet.either import Either, Left, Right
from unittest.mock import patch



def test_invalid_input():
    with pytest.raises(TypeError):
        Either()