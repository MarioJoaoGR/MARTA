
import pytest
from ansible.parsing.quoting import unquote

# Test scenario 1: Valid input with double quotes
def test_valid_input_double_quotes():
    result = unquote('"Hello, World!"')
    assert result == "Hello, World!", f"Expected 'Hello, World!', but got {result}"

# Test scenario 2: Valid input with single quotes
def test_valid_input_single_quotes():
    result = unquote("'Hello, World!'")
    assert result == "Hello, World!", f"Expected 'Hello, World!', but got {result}"

# Test scenario 3: Invalid input without any quotes
def test_invalid_input_no_quotes():
    result = unquote('Hello, World!')
    assert result == 'Hello, World!', f"Expected 'Hello, World!', but got {result}"
