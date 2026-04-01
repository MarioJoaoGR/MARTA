
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this module contains the class and its methods

def test_decode_empty_string():
    with pytest.raises(ValueError):
        result = __RomanNumbers().decode('')
