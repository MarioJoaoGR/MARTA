
import pytest
from sty import RgbFg

def test_edge_cases():
    invalid_colors = [RgbFg(-1, 0, 0), RgbFg(256, 0, 0), RgbFg(0, -1, 0), RgbFg(0, 256, 0), RgbFg(0, 0, -1), RgbFg(0, 0, 256)]
    
    for color in invalid_colors:
        with pytest.raises(ValueError):
            assert color.args == [color.r, color.g, color.b]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_rendertype_RgbFg___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_edge_cases.py:10:34: E1101: Instance of 'RgbFg' has no 'r' member (no-member)
sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_edge_cases.py:10:43: E1101: Instance of 'RgbFg' has no 'g' member (no-member)
sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_edge_cases.py:10:52: E1101: Instance of 'RgbFg' has no 'b' member (no-member)


"""