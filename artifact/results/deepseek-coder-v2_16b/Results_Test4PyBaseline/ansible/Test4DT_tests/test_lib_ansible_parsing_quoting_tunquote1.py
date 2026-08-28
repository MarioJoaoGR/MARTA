
# Module: ansible.parsing.quoting
# test_unquote.py
from ansible.parsing.quoting import unquote

def test_unquote_removes_properly_quoted_double_quotes():
    assert unquote("\"Hello, World!\"") == "Hello, World!"

def test_unquote_removes_properly_quoted_single_quotes():
    assert unquote("'Hello, World!'") == "Hello, World!"

def test_unquote_returns_original_if_not_quoted():
    assert unquote("Hello, World!") == "Hello, World!"

def test_unquote_partially_removes_quotes():
    assert unquote('He said, "Hello!') == 'He said, "Hello!'

def test_unquote_removes_single_quotes():
    assert unquote("He said, 'Hello!'") == "He said, 'Hello!'"

def test_unquote_removes_double_quotes():
    assert unquote('He said, "Hello!"') == 'He said, "Hello!"'

# Additional test case to cover the uncovered line (30)
def test_unquote_handles_empty_string():
    assert unquote("") == ""
