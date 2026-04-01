
import pytest
from string_utils.manipulation import roman_decode

def test_empty_input():
    with pytest.raises(ValueError):
        assert roman_decode('') == 0
