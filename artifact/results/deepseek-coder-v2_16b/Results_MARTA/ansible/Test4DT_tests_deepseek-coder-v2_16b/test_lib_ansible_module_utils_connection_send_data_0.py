
import pytest
from ansible.module_utils.connection import send_data
import struct

def test_valid_string_input():
    input_data = "Hello, World!"
    sock = None  # Assuming a real socket object for testing
    expected_length = len(bytes(input_data, 'utf-8'))
    
    with pytest.raises(AttributeError):
        assert send_data(sock, input_data) == expected_length

def test_valid_list_input():
    input_data = [1, 2, 3]
    sock = None  # Assuming a real socket object for testing
    expected_length = len(bytes(input_data))
    
    with pytest.raises(AttributeError):
        assert send_data(sock, input_data) == expected_length
