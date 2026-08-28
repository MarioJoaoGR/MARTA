
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