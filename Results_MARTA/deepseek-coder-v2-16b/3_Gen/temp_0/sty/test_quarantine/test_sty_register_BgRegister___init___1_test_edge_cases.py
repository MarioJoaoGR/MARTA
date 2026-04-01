
from sty import BgRegister, Style, Sgr, EightbitBg, RgbBg
import pytest

def test_edge_cases():
    bg = BgRegister()
    
    assert isinstance(bg.black, Style)
    assert isinstance(bg.red, Style)
    assert isinstance(bg.green, Style)
    assert isinstance(bg.yellow, Style)
    assert isinstance(bg.blue, Style)
    assert isinstance(bg.magenta, Style)
    assert isinstance(bg.cyan, Style)
    assert isinstance(bg.li_grey, Style)
    assert isinstance(bg.rs, Style)
    assert isinstance(bg.da_grey, Style)
    assert isinstance(bg.li_red, Style)
    assert isinstance(bg.li_green, Style)
    assert isinstance(bg.li_yellow, Style)
    assert isinstance(bg.li_blue, Style)
    assert isinstance(bg.li_magenta, Style)
    assert isinstance(bg.li_cyan, Style)
    assert isinstance(bg.white, Style)
    assert isinstance(bg.da_black, Style)
    assert isinstance(bg.da_red, Style)
    assert isinstance(bg.da_green, Style)
    assert isinstance(bg.da_yellow, Style)
    assert isinstance(bg.da_blue, Style)
    assert isinstance(bg.da_magenta, Style)
    assert isinstance(bg.da_cyan, Style)
    assert isinstance(bg.grey, Style)
    
    # Check if the styles are correctly initialized with their respective Sgr or EightbitBg/RgbBg instances
    assert bg.black.sgr == 40
    assert bg.red.sgr == 41
    assert bg.green.sgr == 42
    assert bg.yellow.sgr == 43
    assert bg.blue.sgr == 44
    assert bg.magenta.sgr == 45
    assert bg.cyan.sgr == 46
    assert bg.li_grey.sgr == 47
    assert bg.rs.sgr == 49
    assert bg.da_grey.sgr == 100
    assert bg.li_red.sgr == 101
    assert bg.li_green.sgr == 102
    assert bg.li_yellow.sgr == 103
    assert bg.li_blue.sgr == 104
    assert bg.li_magenta.sgr == 105
    assert bg.li_cyan.sgr == 106
    assert bg.white.sgr == 107
    assert bg.da_black.eightbit_bg == 0
    assert bg.da_red.eightbit_bg == 88
    assert bg.da_green.eightbit_bg == 22
    assert bg.da_yellow.eightbit_bg == 58
    assert bg.da_blue.eightbit_bg == 18
    assert bg.da_magenta.eightbit_bg == 89
    assert bg.da_cyan.eightbit_bg == 23
    assert bg.grey.eightbit_bg == 249

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_BgRegister___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:35:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:36:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:37:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:38:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:39:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:40:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:41:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:42:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:43:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:44:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:45:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:46:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:47:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:48:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:49:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:50:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:51:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:52:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:53:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:54:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:55:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:56:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:57:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:58:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:59:11: E1101: Instance of 'Style' has no 'eightbit_bg' member (no-member)


"""