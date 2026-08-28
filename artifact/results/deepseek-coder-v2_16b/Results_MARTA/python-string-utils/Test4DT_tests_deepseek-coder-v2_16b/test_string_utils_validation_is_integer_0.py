
import pytest
from string_utils.validation import is_integer

def test_valid_positive_integer():
    assert is_integer('42') == True, "Expected True for valid positive integer '42'"

def test_valid_negative_integer():
    assert is_integer('-42') == True, "Expected True for valid negative integer '-42'"

def test_invalid_floating_point():
    assert is_integer('3.0') == False, "Expected False for invalid floating point '3.0'"
