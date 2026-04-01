
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is the correct module path

def test_valid_case_2():
    roman = __RomanNumbers()
    
    assert roman.encode(58) == 'LVIII'
    assert roman.encode(37) == 'XXXVII'
    assert roman.encode(40) == 'XL'
    assert roman.encode(90) == 'XC'
    assert roman.encode(1994) == 'MCMXCIV'
