
import pytest
from unittest.mock import patch
from httpie.legacy.v3_2_0_session_header_format import post_process

def test_valid_input_original_type_dict():
    # Test case for when original_type is a subclass of dict
    headers = [{'name': 'Content-Type', 'value': 'application/json'}]
    result = post_process(headers, original_type=dict)
    assert result == {'Content-Type': 'application/json'}

def test_valid_input_original_type_custom():
    # Test case for when original_type is a custom class
    class CustomHeader:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    
    headers = [{'name': 'Custom-Header', 'value': 'example'}]
    result = post_process(headers, original_type=CustomHeader)
    assert result == [{'name': 'Custom-Header', 'value': 'example'}]
