
import pytest
from string_utils.manipulation import roman_encode  # Assuming this is the correct module path

def test_valid_case_2():
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode(2020) == 'MMXX'
