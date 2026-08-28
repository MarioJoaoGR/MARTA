
import pytest
from ansible.parsing.quoting import is_quoted

# Test cases for the `is_quoted` function
def test_is_quoted_properly_quoted_double():
    assert is_quoted("\"Hello, World!\"") == True

def test_is_quoted_properly_quoted_single():
    assert is_quoted('"Hello, World!"') == True

def test_is_quoted_properly_quoted_single2():
    assert is_quoted("'Hello, World!'") == True

def test_is_quoted_not_quoted():
    assert is_quoted("Hello, World!") == False

def test_is_quoted_non_quoted_double():
    assert is_quoted('He said, "Hello!"') == False

def test_is_quoted_properly_quoted_single_no_escape():
    assert is_quoted("He said, 'Hello!'") == True

def test_is_quoted_non_quoted_due_to_escape():
    assert is_quoted('He said, "Hello!"') == False
