
import pytest
from unittest.mock import patch
from pymonet.either import Right


def test_invalid_input():
    with pytest.raises(TypeError):
        Right()  # This should raise a TypeError as expected
