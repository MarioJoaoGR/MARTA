
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is the correct path and module name

def test_valid_case_1234():
    roman = __RomanNumbers()
    assert roman.encode(1234) == 'MCCXXXIV'
