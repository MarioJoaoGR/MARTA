# Module: ansible.module_utils.common.text.converters
# Import the function using its provided module name.
from ansible.module_utils.common.text.converters import container_to_text
import pytest

# Test cases for container_to_text function

def test_container_to_text_basic_dict():
    # Basic Usage with a Dictionary:
    result = container_to_text({'key': b'\xe4\xf6\xfc'})
    assert result == {'key': 'äöü'}

def test_container_to_text_list_tuple():
    # Handling Lists and Tuples:
    result_list = container_to_text([b'\xe4\xf6\xfc', 123])
    assert result_list == ['äöü', 123]
    
    result_tuple = container_to_text((b'\xe4\xf6\xfc', 123))
    assert result_tuple == ('äöü', 123)

def test_container_to_text_error_handling():
    # Using Different Error Handling Strategies:
    result = container_to_text(b'\xe4\xf6\xfc', errors='surrogate_or_replace')
    assert result == 'äöü'
    
def test_container_to_text_invalid_input():
    # Test with invalid input (non-byte string) to ensure error handling works correctly
    with pytest.raises(TypeError):  # Assuming the function raises TypeError for non-bytes input without default encoding
        container_to_text('invalid string', errors='strict')
