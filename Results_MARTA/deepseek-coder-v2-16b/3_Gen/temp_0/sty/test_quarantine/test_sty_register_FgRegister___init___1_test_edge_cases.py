
import pytest
from sty import FgRegister, Style, Sgr, EightbitFg, RgbFg
import renderfunc

class TestFgRegisterInit:
    def test_init(self):
        fg = FgRegister()
        
        assert isinstance(fg.black, Style)
        assert fg.black.sgr == Sgr(30)
        
        assert isinstance(fg.red, Style)
        assert fg.red.sgr == Sgr(31)
        
        assert isinstance(fg.green, Style)
        assert fg.green.sgr == Sgr(32)
        
        assert isinstance(fg.yellow, Style)
        assert fg.yellow.sgr == Sgr(33)
        
        assert isinstance(fg.blue, Style)
        assert fg.blue.sgr == Sgr(34)
        
        assert isinstance(fg.magenta, Style)
        assert fg.magenta.sgr == Sgr(35)
        
        assert isinstance(fg.cyan, Style)
        assert fg.cyan.sgr == Sgr(36)
        
        assert isinstance(fg.li_grey, Style)
        assert fg.li_grey.sgr == Sgr(37)
        
        assert isinstance(fg.rs, Style)
        assert fg.rs.sgr == Sgr(39)
        
        assert isinstance(fg.da_grey, Style)
        assert fg.da_grey.sgr == Sgr(90)
        
        assert isinstance(fg.li_red, Style)
        assert fg.li_red.sgr == Sgr(91)
        
        assert isinstance(fg.li_green, Style)
        assert fg.li_green.sgr == Sgr(92)
        
        assert isinstance(fg.li_yellow, Style)
        assert fg.li_yellow.sgr == Sgr(93)
        
        assert isinstance(fg.li_blue, Style)
        assert fg.li_blue.sgr == Sgr(94)
        
        assert isinstance(fg.li_magenta, Style)
        assert fg.li_magenta.sgr == Sgr(95)
        
        assert isinstance(fg.li_cyan, Style)
        assert fg.li_cyan.sgr == Sgr(96)
        
        assert isinstance(fg.white, Style)
        assert fg.white.sgr == Sgr(97)
        
        assert isinstance(fg.da_black, Style)
        assert fg.da_black.eightbit_fg == EightbitFg(0)
        
        assert isinstance(fg.da_red, Style)
        assert fg.da_red.eightbit_fg == EightbitFg(88)
        
        assert isinstance(fg.da_green, Style)
        assert fg.da_green.eightbit_fg == EightbitFg(22)
        
        assert isinstance(fg.da_yellow, Style)
        assert fg.da_yellow.eightbit_fg == EightbitFg(58)
        
        assert isinstance(fg.da_blue, Style)
        assert fg.da_blue.eightbit_fg == EightbitFg(18)
        
        assert isinstance(fg.da_magenta, Style)
        assert fg.da_magenta.eightbit_fg == EightbitFg(89)
        
        assert isinstance(fg.da_cyan, Style)
        assert fg.da_cyan.eightbit_fg == EightbitFg(23)
        
        assert isinstance(fg.grey, Style)
        assert fg.grey.eightbit_fg == EightbitFg(249)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_FgRegister___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:4:0: E0401: Unable to import 'renderfunc' (import-error)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:11:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:14:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:17:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:20:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:23:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:26:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:29:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:32:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:35:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:38:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:41:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:44:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:47:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:50:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:53:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:56:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:59:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:62:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:65:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:68:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:71:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:74:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:77:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:80:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_edge_cases.py:83:15: E1101: Instance of 'Style' has no 'eightbit_fg' member (no-member)


"""