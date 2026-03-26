
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is the correct path to the module

def test_valid_case_3999():
    roman = __RomanNumbers()
    assert roman.encode(3999) == 'MMMCMXCIX'
