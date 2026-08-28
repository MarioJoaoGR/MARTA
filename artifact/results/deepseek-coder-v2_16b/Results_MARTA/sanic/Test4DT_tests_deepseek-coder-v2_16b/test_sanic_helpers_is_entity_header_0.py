
import pytest
from sanic.helpers import is_entity_header

# List of predefined entity headers for testing
_ENTITY_HEADERS = {'content-type', 'content-length', 'content-encoding'}

def test_valid_input():
    header = 'Content-Type'
    assert is_entity_header(header) == True

def test_case_insensitivity():
    header = 'content-type'
    assert is_entity_header(header) == True

def test_non_entity_header():
    header = 'X-Custom-Header'
    assert is_entity_header(header) == False
