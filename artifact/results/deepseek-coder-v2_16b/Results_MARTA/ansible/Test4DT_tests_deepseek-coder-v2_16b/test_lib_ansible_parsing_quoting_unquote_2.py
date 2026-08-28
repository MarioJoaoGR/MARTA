
import pytest
from ansible.parsing.quoting import unquote

# Test scenario 1: Test standard input with double quotes
def test_valid_input_double_quotes():
    assert unquote("\"Hello, World!\"") == "Hello, World!"

# Test scenario 2: Test standard input with single quotes
def test_valid_input_single_quotes():
    assert unquote('\'Hello, World!\'') == 'Hello, World!'

# Test scenario 3: Test input without any quotes
def test_invalid_input_no_quotes():
    assert unquote("Hello, World!") == "Hello, World!"
