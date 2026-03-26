
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is the correct path to the module

def test_invalid_input_string():
    with pytest.raises(ValueError) as excinfo:
        result = __RomanNumbers().encode('abc')
    assert str(excinfo.value) == 'Invalid input, only strings or integers are allowed'
