
import pytest
from string_utils.manipulation import __RomanNumbers

def test_valid_case_1():
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode('42') == 'XLII'
    assert __RomanNumbers.encode(1976) == 'MCMLXXVI'
