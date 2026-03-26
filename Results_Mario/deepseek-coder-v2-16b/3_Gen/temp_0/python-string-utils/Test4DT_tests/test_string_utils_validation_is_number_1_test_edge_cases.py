
import pytest
from string_utils.validation import is_number

def test_edge_cases():
    # Test valid numbers
    assert is_number('42') == True
    assert is_number('19.99') == True
    assert is_number('-9.12') == True
    assert is_number('1e3') == True
    
    # Test invalid strings
    assert is_number('1 2 3') == False
    assert is_number('abc') == False
    assert is_number('1a2b3c') == False
    assert is_number('') == False
