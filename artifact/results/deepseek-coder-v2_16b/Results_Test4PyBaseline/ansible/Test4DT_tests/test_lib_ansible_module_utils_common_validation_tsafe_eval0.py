
import pytest
from ansible.module_utils.common.validation import safe_eval
from ast import literal_eval
import re
from six import string_types

# Test cases for basic evaluation
def test_safe_eval_basic():
    result = safe_eval("42")
    assert result == 42

def test_safe_eval_with_locals():
    local_vars = {'x': 10}
    result = safe_eval("x + 5", locals=local_vars)
    assert result == 15

# Test cases for handling exceptions explicitly
def test_safe_eval_import_os():
    with pytest.raises(SyntaxError):
        safe_eval("import os")

def test_safe_eval_include_exceptions():
    try:
        result, exception = safe_eval("import os", include_exceptions=True)
        assert result is None
        assert isinstance(exception, ImportError)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

# Test cases for evaluating a list
def test_safe_eval_list():
    result = safe_eval("[1, 2, 3]")
    assert result == [1, 2, 3]

# Test cases for handling method calls to modules
def test_safe_eval_os_system():
    with pytest.raises(ImportError):
        safe_eval("os.system('ls')")

def test_safe_eval_include_exceptions_method_call():
    try:
        result, exception = safe_eval("os.system('ls')", include_exceptions=True)
        assert result is None
        assert isinstance(exception, ImportError)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

# Additional test cases to cover different scenarios
def test_safe_eval_invalid_expression():
    with pytest.raises(SyntaxError):
        safe_eval("x = 10")

def test_safe_eval_include_exceptions_invalid_expression():
    try:
        result, exception = safe_eval("x = 10", include_exceptions=True)
        assert result is None
        assert isinstance(exception, SyntaxError)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

def test_safe_eval_literal_eval_error():
    with pytest.raises(ValueError):
        safe_eval("invalid expression")

def test_safe_eval_include_exceptions_literal_eval_error():
    try:
        result, exception = safe_eval("invalid expression", include_exceptions=True)
        assert result is None
        assert isinstance(exception, ValueError)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")
