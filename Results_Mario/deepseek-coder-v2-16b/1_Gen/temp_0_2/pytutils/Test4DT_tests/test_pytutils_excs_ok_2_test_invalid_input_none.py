
import pytest
from pytutils.excs import ok
from unittest.mock import patch

def test_invalid_input_none():
    with pytest.raises(TypeError):
        with ok():
            raise TypeError("This is a TypeError")
