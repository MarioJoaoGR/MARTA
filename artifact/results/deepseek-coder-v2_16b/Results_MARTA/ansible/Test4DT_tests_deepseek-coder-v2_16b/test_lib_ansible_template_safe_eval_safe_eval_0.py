
import pytest
import ast
import builtins
from ansible.template import safe_eval

# Test scenarios
def test_valid_expression():
    expr = '1 + 2'
    result = safe_eval(expr)
    assert result == 3

def test_invalid_expression():
    expr = 'this is not a valid expression'
    with pytest.raises(Exception):
        safe_eval(expr)

def test_include_exceptions():
    expr = '1 / 0'
    result, error = safe_eval(expr, include_exceptions=True)
    assert isinstance(error, ZeroDivisionError)
