
from typing import Union
import pytest
from string_utils.manipulation import __RomanNumbers

def test_invalid_input_1():
    with pytest.raises(ValueError):
        assert __RomanNumbers.encode('0')  # This should raise ValueError as per the function's validation logic
