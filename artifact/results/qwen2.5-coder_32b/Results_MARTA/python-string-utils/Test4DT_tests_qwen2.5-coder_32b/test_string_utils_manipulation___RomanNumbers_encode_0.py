
import pytest
from string_utils.manipulation import __RomanNumbers

def test_valid_cases():
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode('58') == 'LVIII'
    assert __RomanNumbers.encode(1994) == 'MCMXCIV'
    assert __RomanNumbers.encode('3999') == 'MMMCMXCIX'

def test_edge_cases():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode('3999') == 'MMMCMXCIX'
    assert __RomanNumbers.encode('1000') == 'M'
    assert __RomanNumbers.encode(500) == 'D'

def test_invalid_cases():
    with pytest.raises(ValueError):
        __RomanNumbers.encode(0)
    
    with pytest.raises(ValueError):
        __RomanNumbers.encode(4000)
    
    with pytest.raises(ValueError):
        __RomanNumbers.encode('')
    
    with pytest.raises(ValueError):
        __RomanNumbers.encode(None)
    
    with pytest.raises(ValueError):
        __RomanNumbers.encode('abc')
