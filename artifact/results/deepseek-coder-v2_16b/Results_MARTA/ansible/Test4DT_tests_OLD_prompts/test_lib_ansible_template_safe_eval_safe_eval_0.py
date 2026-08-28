
import pytest
from ansible.template import safe_eval
import builtins
import ast
from typing import Any, Tuple, Union

def test_basic_evaluation():
    result = safe_eval("1 + 2")
    assert result == 3


def test_including_exceptions_for_debugging():
    try:
        result, error = safe_eval("1 / 0", include_exceptions=True)
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)
