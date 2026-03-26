
import pytest
from isort.core import _has_changed

def remove_whitespace(text, line_separator):
    return "".join(text.split())

@pytest.mark.parametrize("before, after, expected", [
    ("Hello, World!", "Hello, World!", False),
    (" Hello, World! ", "Hello, World!", True),
    ("Hello, World!\n", "Hello, World!\n", False),
    ("Hello, World!", "Hello, World!\n", True),
    ("Hello, World!", "Hello, World!", False, line_separator="."),
    ("Hello, World!", "Hello, World!\n", True, line_separator="."),
    (" Hello, World! ", "Hello, World!", True, ignore_whitespace=True),
    ("Hello, World!", "Hello, World!", False, ignore_whitespace=True)
])
def test__has_changed_basic(before, after, expected):
    assert _has_changed(before, after) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_core__has_changed_0_test__has_changed_basic
isort/Test4DT_tests/test_isort_core__has_changed_0_test__has_changed_basic.py:13:47: E0001: Parsing failed: 'invalid syntax. Maybe you meant '==' or ':=' instead of '='? (Test4DT_tests.test_isort_core__has_changed_0_test__has_changed_basic, line 13)' (syntax-error)


"""