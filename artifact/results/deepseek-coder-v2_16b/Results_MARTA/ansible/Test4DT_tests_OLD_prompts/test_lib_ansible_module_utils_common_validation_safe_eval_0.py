
import pytest
from ansible.module_utils.common.validation import safe_eval
import re
from ast import literal_eval

def test_safe_eval_simple_literal():
    result = safe_eval("42")
    assert result == 42

def test_safe_eval_array_literal():
    result = safe_eval("[1, 2, 3]")
    assert result == [1, 2, 3]

