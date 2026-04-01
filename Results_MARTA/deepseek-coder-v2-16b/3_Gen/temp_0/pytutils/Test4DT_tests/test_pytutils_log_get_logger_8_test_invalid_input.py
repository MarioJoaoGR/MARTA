
import logging
from pytutils.log import get_logger  # Assuming this module exists and has the get_logger function
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        log = get_logger(123)  # Providing an integer instead of a string
