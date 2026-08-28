
import pytest
from string_utils.validation import is_decimal

def test_is_decimal_basic():
    assert is_decimal('42.0') == True, "Test case '42.0' failed"
    assert is_decimal('-9.12') == True, "Test case '-9.12' failed"
    assert is_decimal('1e3') == False, "Test case '1e3' failed"
    assert is_decimal('42') == False, "Test case '42' failed"
