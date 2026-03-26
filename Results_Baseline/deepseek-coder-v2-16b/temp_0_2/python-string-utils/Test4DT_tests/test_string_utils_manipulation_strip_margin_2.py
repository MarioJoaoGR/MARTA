
# Module: string_utils.manipulation
# test_string_utils.py
from string_utils.manipulation import strip_margin, InvalidInputError
import pytest  # Importing pytest at the beginning of the file

def test_strip_margin_invalid_input():
    """Test that strip_margin raises an InvalidInputError for non-string input."""
    invalid_inputs = [None, 123, [], {}]
    for invalid_input in invalid_inputs:
        with pytest.raises(InvalidInputError):
            strip_margin(invalid_input)
