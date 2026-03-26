
from sty import rendertype
import pytest

def test_valid_input():
    # Create an instance of EightbitBg with a valid number
    bg_color = rendertype.EightbitBg(123)
    
    # Assert that the num attribute is correctly set to 123
    assert bg_color.num == 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_rendertype_EightbitBg___init___0_test_valid_input
sty/Test4DT_tests/test_sty_rendertype_EightbitBg___init___0_test_valid_input.py:10:11: E1101: Instance of 'EightbitBg' has no 'num' member (no-member)


"""