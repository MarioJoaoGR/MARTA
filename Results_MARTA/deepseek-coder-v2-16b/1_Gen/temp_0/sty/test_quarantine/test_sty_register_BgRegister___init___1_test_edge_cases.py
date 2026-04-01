
import pytest
from sty import register
from sty.style import Style, Sgr, EightbitBg, RgbBg
from sty.renderfunc import sgr, eightbit_bg, rgb_bg

@pytest.fixture(scope="module")
def bg_register():
    return register.BgRegister()

def test_init_bg_register(bg_register):
    assert isinstance(bg_register.black, Style)
    assert isinstance(bg_register.red, Style)
    assert isinstance(bg_register.green, Style)
    assert isinstance(bg_register.yellow, Style)
    assert isinstance(bg_register.blue, Style)
    assert isinstance(bg_register.magenta, Style)
    assert isinstance(bg_register.cyan, Style)
    assert isinstance(bg_register.li_grey, Style)
    assert isinstance(bg_register.rs, Style)
    assert isinstance(bg_register.da_grey, Style)
    assert isinstance(bg_register.li_red, Style)
    assert isinstance(bg_register.li_green, Style)
    assert isinstance(bg_register.li_yellow, Style)
    assert isinstance(bg_register.li_blue, Style)
    assert isinstance(bg_register.li_magenta, Style)
    assert isinstance(bg_register.li_cyan, Style)
    assert isinstance(bg_register.white, Style)
    assert isinstance(bg_register.da_black, Style)
    assert isinstance(bg_register.da_red, Style)
    assert isinstance(bg_register.da_green, Style)
    assert isinstance(bg_register.da_yellow, Style)
    assert isinstance(bg_register.da_blue, Style)
    assert isinstance(bg_register.da_magenta, Style)
    assert isinstance(bg_register.da_cyan, Style)
    assert isinstance(bg_register.grey, Style)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_BgRegister___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:4:0: E0401: Unable to import 'sty.style' (import-error)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:4:0: E0611: No name 'style' in module 'sty' (no-name-in-module)

"""