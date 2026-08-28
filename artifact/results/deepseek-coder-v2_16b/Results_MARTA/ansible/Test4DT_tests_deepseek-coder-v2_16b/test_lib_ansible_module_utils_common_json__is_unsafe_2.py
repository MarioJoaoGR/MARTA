
import pytest

def _is_unsafe(value):
    return getattr(value, '__UNSAFE__', False) and not getattr(value, '__ENCRYPTED__', False)

# Test 1: Valid input where value has __UNSAFE__ set to True and not __ENCRYPTED__
class ExampleClass:
    __UNSAFE__ = True

def test_valid_input_happy_path():
    assert _is_unsafe(ExampleClass()) == True

# Test 2: Edge case where input is None
def test_edge_case_none():
    assert _is_unsafe(None) == False

# Test 3: Invalid input where value has __UNSAFE__ set to False and __ENCRYPTED__ set to True
class SafeClass:
    __UNSAFE__ = False
    __ENCRYPTED__ = True

def test_invalid_input_error_handling():
    assert _is_unsafe(SafeClass()) == False
