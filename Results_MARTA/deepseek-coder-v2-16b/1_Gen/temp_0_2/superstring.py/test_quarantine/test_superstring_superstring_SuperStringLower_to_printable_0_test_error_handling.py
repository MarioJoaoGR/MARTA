
import pytest
from superstring.superstring import SuperString
from superstring.superstring_lower import SuperStringLower

def test_to_printable_with_default_indices():
    s = SuperStringLower(SuperString("Hello, World!"))
    assert s.to_printable() == "hello, world!"

def test_to_printable_with_specified_indices():
    s = SuperStringLower(SuperString("Hello, World!"))
    assert s.to_printable(2, 8) == "llo, w"

def test_to_printable_empty_string():
    s = SuperStringLower(SuperString(""))
    assert s.to_printable() == ""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringLower_to_printable_0_test_error_handling
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_error_handling.py:4:0: E0401: Unable to import 'superstring.superstring_lower' (import-error)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_error_handling.py:4:0: E0611: No name 'superstring_lower' in module 'superstring' (no-name-in-module)


"""