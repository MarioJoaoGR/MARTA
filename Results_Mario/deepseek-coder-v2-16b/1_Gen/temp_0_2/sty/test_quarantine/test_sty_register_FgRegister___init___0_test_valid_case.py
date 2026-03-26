
import pytest
from sty import register, Style, Sgr, EightbitFg, RgbFg
import renderfunc

class MockRenderFunc:
    @staticmethod
    def sgr(sgr_code):
        return f"\033[{sgr_code}m"
    
    @staticmethod
    def eightbit_fg(color_code):
        return f"\033[38;5;{color_code}m"
    
    @staticmethod
    def rgb_fg(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

class MockFgRegister(register.FgRegister):
    def __init__(self):
        super().__init__()
        self.renderfuncs = {Sgr: MockRenderFunc.sgr, EightbitFg: MockRenderFunc.eightbit_fg, RgbFg: MockRenderFunc.rgb_fg}
    
    def set_eightbit_call(self, call):
        pass
    
    def set_rgb_call(self, call):
        pass

@pytest.fixture
def fg():
    return MockFgRegister()

def test_valid_case(fg):
    assert str(fg.red) == "\033[31m"
    assert str(fg.green) == "\033[32m"
    assert str(fg.blue) == "\033[34m"
    assert str(fg.white) == "\033[97m"
    assert str(fg.rs) == "\033[39m"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_FgRegister___init___0_test_valid_case
sty/Test4DT_tests/test_sty_register_FgRegister___init___0_test_valid_case.py:4:0: E0401: Unable to import 'renderfunc' (import-error)


"""