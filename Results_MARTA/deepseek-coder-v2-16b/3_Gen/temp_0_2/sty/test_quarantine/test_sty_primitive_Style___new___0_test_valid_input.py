
import pytest
from sty import Style, RgbFg, Sgr, StylingRule
from typing import Iterable

def test_valid_input():
    style = Style(RgbFg(1, 5, 10), Sgr(1))
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == '\x1B[38;2;1;5;10m\x1B[1m'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Style___new___0_test_valid_input
sty/Test4DT_tests/test_sty_primitive_Style___new___0_test_valid_input.py:3:0: E0611: No name 'StylingRule' in module 'sty' (no-name-in-module)


"""