
import pytest
from string_utils.manipulation import __RomanNumbers

def test_valid_case():
    # Test with a valid Roman numeral string that should return its corresponding integer value
    assert __RomanNumbers().decode('IX') == 9
    
    # Add more test cases to cover different scenarios and edge cases
    assert __RomanNumbers().decode('IV') == 4
    assert __RomanNumbers().decode('MCMXCIV') == 1994
    assert __RomanNumbers().decode('LVIII') == 58
    
    # Test with an invalid input to ensure it raises a ValueError
    with pytest.raises(ValueError):
        __RomanNumbers().decode('')
        
    with pytest.raises(ValueError):
        __RomanNumbers().decode(None)
        
    with pytest.raises(ValueError):
        __RomanNumbers().decode(' ')
