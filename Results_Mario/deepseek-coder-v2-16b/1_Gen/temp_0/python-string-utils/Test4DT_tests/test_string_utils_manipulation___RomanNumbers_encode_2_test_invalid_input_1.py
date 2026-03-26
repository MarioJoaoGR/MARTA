
import pytest
from string_utils.manipulation import __RomanNumbers

def test_invalid_input_1():
    with pytest.raises(ValueError):
        assert __RomanNumbers.encode('0')  # This should raise ValueError

    with pytest.raises(ValueError):
        assert __RomanNumbers.encode(4000)  # This should also raise ValueError
