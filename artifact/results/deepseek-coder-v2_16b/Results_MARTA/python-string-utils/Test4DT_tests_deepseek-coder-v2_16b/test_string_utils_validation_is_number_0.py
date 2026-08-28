
import pytest
from string_utils.validation import is_number

def test_valid_numbers():
    input_string = '123'
    assert is_number(input_string) == True, f"Expected {input_string} to be a valid number."
    
    input_string = '123.45'
    assert is_number(input_string) == True, f"Expected {input_string} to be a valid number."
    
    input_string = '-123.45e6'
    assert is_number(input_string) == True, f"Expected {input_string} to be a valid number."

def test_invalid_inputs():
    input_string = 'abc'
    assert is_number(input_string) == False, f"Expected {input_string} to be an invalid number."
    
    input_string = '123abc'
    assert is_number(input_string) == False, f"Expected {input_string} to be an invalid number."
    
    input_string = '12.34e56f'
    assert is_number(input_string) == False, f"Expected {input_string} to be an invalid number."

def test_error_handling():
    with pytest.raises(TypeError):
        is_number(None)
