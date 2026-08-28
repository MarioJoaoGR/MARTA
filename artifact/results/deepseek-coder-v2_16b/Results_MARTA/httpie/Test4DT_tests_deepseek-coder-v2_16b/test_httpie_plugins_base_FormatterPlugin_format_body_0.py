
import pytest
from httpie.plugins.base import FormatterPlugin
import requests

def test_valid_input():
    formatter = FormatterPlugin(format_options={'headers': True, 'body': False})
    response = requests.Response()
    response._content = b'{"key": "value"}'
    response.encoding = 'utf-8'
    response.headers['Content-Type'] = 'application/json'
    
    formatted_response = formatter.format_body(str(response._content, encoding='utf-8'), response.headers['Content-Type'])
    
    assert isinstance(formatted_response, str), "Expected a string representation of the body"
    assert '"key": "value"' in formatted_response, "Expected the body to include key 'key' with value 'value'"

def test_edge_case():
    formatter = FormatterPlugin(format_options={'headers': True, 'body': False})
    response = requests.Response()
    response._content = None
    response.encoding = 'utf-8'
    response.headers['Content-Type'] = 'application/json'
    
    formatted_response = formatter.format_body(str(response._content), response.headers['Content-Type'])
    
    assert isinstance(formatted_response, str) or formatted_response is None, "Expected a string representation of the body or None if there's no content"
    assert '"key": "value"' not in formatted_response, "No expected key 'key' with value 'value' should be present when there's no body content"
