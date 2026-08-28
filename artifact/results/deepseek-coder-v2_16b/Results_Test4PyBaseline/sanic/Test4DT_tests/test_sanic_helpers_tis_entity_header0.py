
import pytest
from sanic.helpers import is_entity_header

# Define a list of entity headers for testing purposes
_ENTITY_HEADERS = ["content-type", "x-custom-header", "accept"]

def test_is_entity_header_true():
    assert is_entity_header("Content-Type") == True