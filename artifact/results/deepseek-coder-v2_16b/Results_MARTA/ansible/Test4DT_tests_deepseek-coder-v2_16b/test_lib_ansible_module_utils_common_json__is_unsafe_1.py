
import pytest
from unittest.mock import patch

def _is_unsafe(value):
    return getattr(value, '__UNSAFE__', False) and not getattr(value, '__ENCRYPTED__', False)

# Test 1: Valid input where value has __UNSAFE__ set to True and not __ENCRYPTED__
class ExampleClass:
    __UNSAFE__ = True

def test_valid_input_happy_path():
    assert _is_unsafe(ExampleClass()) == True

# Test 2: Test with None input to check error handling
def test_edge_case_none():
    assert _is_unsafe(None) == False

# Test 3: Test with invalid input type to check error handling
def test_invalid_input_error_handling():
    assert _is_unsafe('string') == False
