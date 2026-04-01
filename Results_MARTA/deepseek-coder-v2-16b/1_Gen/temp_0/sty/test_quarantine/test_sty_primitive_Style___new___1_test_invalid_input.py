
from sty import Style, StylingRule  # Importing from the correct module
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        Style("invalid input")  # This should raise a TypeError because "invalid input" is not of type StylingRule

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Style___new___1_test_invalid_input
sty/Test4DT_tests/test_sty_primitive_Style___new___1_test_invalid_input.py:2:0: E0611: No name 'StylingRule' in module 'sty' (no-name-in-module)

"""