
import pytest
from string_utils.validation import is_integer

# Test cases for valid integers
def test_valid_positive_integers():
    assert is_integer('42') == True
    assert is_integer('-42') == True