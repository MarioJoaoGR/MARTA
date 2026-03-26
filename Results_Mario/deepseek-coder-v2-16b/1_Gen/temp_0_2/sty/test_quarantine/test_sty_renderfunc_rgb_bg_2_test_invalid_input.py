
import pytest
from sty import rgb_bg

def test_invalid_input():
    # Test with invalid RGB values (out of range)
    with pytest.raises(ValueError):
        assert rgb_bg(-1, 256, 0)
    with pytest.raises(ValueError):
        assert rgb_bg(256, 0, 0)
    with pytest.raises(ValueError):
        assert rgb_bg(0, -1, 0)
    with pytest.raises(ValueError):
        assert rgb_bg(0, 256, 0)
    with pytest.raises(ValueError):
        assert rgb_bg(0, 0, -1)
    with pytest.raises(ValueError):
        assert rgb_bg(0, 0, 256)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_renderfunc_rgb_bg_2_test_invalid_input
sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_2_test_invalid_input.py:3:0: E0611: No name 'rgb_bg' in module 'sty' (no-name-in-module)


"""