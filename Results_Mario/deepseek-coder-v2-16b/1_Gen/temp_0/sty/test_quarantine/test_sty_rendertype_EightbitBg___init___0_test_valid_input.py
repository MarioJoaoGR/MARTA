
from sty import EightbitBg
import pytest

def test_valid_input():
    # Test valid input by creating an instance of EightbitBg with a number between 0 and 255
    num = 123
    bg_color = EightbitBg(num)
    
    # Assert that the created object has the attribute 'num' and it matches the provided value
    assert hasattr(bg_color, 'num')
    assert bg_color.num == num

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_rendertype_EightbitBg___init___0_test_valid_input
sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_valid_input.py:12:11: E1101: Instance of 'EightbitBg' has no 'num' member (no-member)

"""