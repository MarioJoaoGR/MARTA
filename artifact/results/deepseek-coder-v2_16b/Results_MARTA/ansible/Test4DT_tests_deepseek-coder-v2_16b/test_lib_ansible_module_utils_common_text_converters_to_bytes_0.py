
import pytest
from ansible.module_utils.common.text.converters import to_bytes

def test_valid_input_happy_path():
    text_string = 'Hello, World!'
    encoded_bytes = to_bytes(text_string)
    assert isinstance(encoded_bytes, bytes), "Expected a byte string"
    assert encoded_bytes == b'Hello, World!', "Expected the same content as input but in byte format"

def test_edge_cases():
    obj = None
    with pytest.raises(TypeError):
        to_bytes(obj)
    
    empty_list = []
    encoded_bytes = to_bytes(empty_list)
    assert isinstance(encoded_bytes, bytes), "Expected a byte string"
    assert encoded_bytes == b'[]', "Expected the list representation in byte format"

def test_invalid_inputs_error_handling():
    non_string_obj = 42
    with pytest.raises(TypeError):
        to_bytes(non_string_obj)
