
import pytest
from string_utils.manipulation import __RomanNumbers  # Adjust the import path as necessary based on your project structure

def test_valid_case():
    roman_numeral = __RomanNumbers()
    assert roman_numeral.decode('IX') == 9
