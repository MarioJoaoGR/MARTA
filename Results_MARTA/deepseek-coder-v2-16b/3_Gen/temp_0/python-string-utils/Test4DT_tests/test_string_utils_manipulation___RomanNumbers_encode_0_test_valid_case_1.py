
import pytest
from string_utils.manipulation import __RomanNumbers

def test_valid_case_1():
    # Test encoding a number within the valid range (1 to 3999)
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode('42') == 'XLII'
    assert __RomanNumbers.encode(1976) == 'MCMLXXVI'

if __name__ == "__main__":
    pytest.main()
