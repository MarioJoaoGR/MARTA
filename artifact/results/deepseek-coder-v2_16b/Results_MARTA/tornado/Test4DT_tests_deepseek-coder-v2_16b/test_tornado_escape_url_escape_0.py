
import pytest
import urllib.parse
from typing import Union

# Assuming the function is defined in a module named tornado.escape
# If not, adjust the import accordingly
from tornado.escape import url_escape

@pytest.fixture(params=[None, 'Hello, World!', b'Hello, World!'])
def value(request):
    return request.param

def test_valid_input_string(value='Hello, World!'):
    assert url_escape(value) == 'Hello%2C+World%21'

def test_valid_input_byte_sequence(value=b'Hello, World!'):
    assert url_escape(value) == 'Hello%2C+World%21'

def test_invalid_input_none():
    with pytest.raises(TypeError):
        url_escape(None)
