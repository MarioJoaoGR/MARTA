
import pytest
from ansible.template import safe_eval

def test_safe_eval_basic():
    result = safe_eval("1 + 2")
    assert result == 3, f"Expected 3 but got {result}"

def test_safe_eval_with_locals():
    locals_dict = {'a': 5}
    result = safe_eval("a * 2", locals=locals_dict)
    assert result == 10, f"Expected 10 but got {result}"

def test_safe_eval_include_exceptions():
    try:
        result, error = safe_eval("1 / 0", include_exceptions=True)
    except Exception as e:
        assert isinstance(e, ZeroDivisionError), f"Expected ZeroDivisionError but got {type(e)}"
