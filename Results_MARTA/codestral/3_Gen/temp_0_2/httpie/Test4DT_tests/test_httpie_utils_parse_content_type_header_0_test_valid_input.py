
import pytest
from unittest.mock import patch

def parse_content_type_header(header):
    """Borrowed from requests."""
    tokens = header.split(';')
    content_type, params = tokens[0].strip(), tokens[1:]
    params_dict = {}
    items_to_strip = "\"' "
    for param in params:
        param = param.strip()
        if param:
            key, value = param, True
            index_of_equals = param.find("=")
            if index_of_equals != -1:
                key = param[:index_of_equals].strip(items_to_strip)
                value = param[index_of_equals + 1:].strip(items_to_strip)
            params_dict[key.lower()] = value
    return content_type, params_dict

def test_valid_input():
    header = 'text/html; charset=utf-8'
    expected_content_type = 'text/html'
    expected_params = {'charset': 'utf-8'}
    
    with patch('httpie.utils.parse_content_type_header', return_value=(expected_content_type, expected_params)):
        content_type, params_dict = parse_content_type_header(header)
        
        assert content_type == expected_content_type
        assert params_dict == expected_params
