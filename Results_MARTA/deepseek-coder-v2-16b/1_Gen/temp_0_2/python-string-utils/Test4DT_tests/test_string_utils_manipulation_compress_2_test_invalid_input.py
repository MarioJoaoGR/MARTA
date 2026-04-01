
import pytest
from string_utils.manipulation import compress

def test_invalid_input():
    with pytest.raises(ValueError):
        # Test when input string is empty
        compress("")
