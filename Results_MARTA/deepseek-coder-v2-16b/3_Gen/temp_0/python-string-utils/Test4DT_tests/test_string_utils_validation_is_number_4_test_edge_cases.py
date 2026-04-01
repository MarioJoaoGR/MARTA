
import pytest
from string_utils.validation import is_number

def test_edge_cases():
    # Test valid numbers
    assert is_number('42') == True
    assert is_number('19.99') == True
    assert is_number('-9.12') == True
    assert is_number('1e3') == True
    
    # Test invalid numbers
    assert is_number('1 2 3') == False
    assert is_number('abc') == False
    assert is_number('') == False
    assert is_number('+') == False
    assert is_number('-') == False
    assert is_number('.') == False
    assert is_number('e3') == False
    
    # Test invalid types
    with pytest.raises(TypeError):
        is_number(42)
