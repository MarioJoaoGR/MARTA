
import pytest
from unittest.mock import patch
from sanic.helpers import is_entity_header

# Define the predefined list of entity headers for testing purposes
_ENTITY_HEADERS = {"content-type", "Content-Type", "X-Custom-Header"}

def test_valid_case():
    assert is_entity_header("Content-Type") == True

def test_case_insensitivity():
    assert is_entity_header("content-type") == True

def test_non_entity_header():
    assert is_entity_header("X-Custom-Header") == False

def test_empty_string():
    assert is_entity_header("") == False
