
import pytest
from string_utils.validation import is_decimal

def test_is_decimal_positive():
    assert is_decimal('42.0'), "Should be a decimal"
    assert is_decimal('-9.12'), "Should be a decimal"
    assert is_decimal('+0.99'), "Should be a decimal"
    assert is_decimal('.5'), "Should be a decimal"