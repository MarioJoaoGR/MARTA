
import pytest
from string_utils.validation import is_number

def test_valid_number():
    assert is_number('42') == True
    assert is_number('19.99') == True
    assert is_number('-9.12') == True
    assert is_number('1e3') == True
    assert is_number('1 2 3') == False
