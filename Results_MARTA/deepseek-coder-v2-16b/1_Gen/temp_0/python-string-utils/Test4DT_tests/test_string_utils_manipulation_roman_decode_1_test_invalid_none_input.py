
import pytest
from string_utils.manipulation import roman_decode

def test_invalid_none_input():
    with pytest.raises(ValueError):
        roman_decode(None)
