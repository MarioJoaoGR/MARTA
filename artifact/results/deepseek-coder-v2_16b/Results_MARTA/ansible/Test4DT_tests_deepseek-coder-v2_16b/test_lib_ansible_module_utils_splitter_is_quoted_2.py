
import pytest

def is_quoted(data):
    return len(data) > 0 and (data[0] == '"' and data[-1] == '"' or data[0] == "'" and data[-1] == "'")

# Test cases for valid inputs with double quotes, single quotes, and no quotes
def test_valid_case_double_quotes():
    assert is_quoted('"Hello, World!"')  # True, double quotes around the string

def test_valid_case_single_quotes():
    assert is_quoted("'Hello, World!'")  # True, single quotes around the string

def test_invalid_case_no_quotes():
    assert not is_quoted('Hello, World!')  # False, no quotes around the string
