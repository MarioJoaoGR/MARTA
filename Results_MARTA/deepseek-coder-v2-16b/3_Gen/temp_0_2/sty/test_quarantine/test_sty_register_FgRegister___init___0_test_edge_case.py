
import pytest
from sty import register, Style, Sgr, EightbitFg, RgbFg

@pytest.mark.parametrize("input_value", [None, []])
def test_edge_case(input_value):
    with pytest.raises(TypeError):
        fg = FgRegister()
        if input_value is not None:
            fg.__init__(input_value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_FgRegister___init___0_test_edge_case
sty/Test4DT_tests/test_sty_register_FgRegister___init___0_test_edge_case.py:8:13: E0602: Undefined variable 'FgRegister' (undefined-variable)


"""