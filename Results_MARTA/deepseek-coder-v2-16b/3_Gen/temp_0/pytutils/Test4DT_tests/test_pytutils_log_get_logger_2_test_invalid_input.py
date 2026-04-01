
import pytest
import logging
from pytutils.log import get_logger  # Assuming this module exists and has the function defined

def test_invalid_input():
    with pytest.raises(TypeError):  # Since we expect a TypeError for non-string inputs
        log = get_logger(123)  # Providing an integer as input, which is invalid
