
import pytest
from string_utils.manipulation import strip_margin, InvalidInputError
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_margin(123)  # Expects a string input but provides an integer
