
import pytest
from string_utils.manipulation import __RomanNumbers  # Adjust the import according to your module structure

def test_valid_case():
    assert __RomanNumbers.decode('XIV') == 14
    assert __RomanNumbers.decode('XXVII') == 27
    assert __RomanNumbers.decode('XLII') == 42
    assert __RomanNumbers.decode('XCIX') == 99
    assert __RomanNumbers.decode('MMMCMXCIX') == 3999

def test_invalid_input():
    with pytest.raises(ValueError):
        __RomanNumbers.decode('')
    with pytest.raises(ValueError):
        __RomanNumbers.decode(None)
    with pytest.raises(ValueError):
        __RomanNumbers.decode(1234)  # Non-string input
