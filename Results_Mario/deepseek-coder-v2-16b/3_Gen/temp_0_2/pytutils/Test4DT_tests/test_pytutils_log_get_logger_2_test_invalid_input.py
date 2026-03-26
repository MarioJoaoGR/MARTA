
import pytest
from pytutils.log import get_logger

def test_invalid_input():
    with pytest.raises(TypeError):
        get_logger(123)  # Passing an integer instead of a string should raise TypeError
