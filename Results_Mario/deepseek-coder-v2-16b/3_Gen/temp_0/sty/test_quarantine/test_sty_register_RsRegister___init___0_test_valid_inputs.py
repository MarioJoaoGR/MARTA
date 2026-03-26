
import pytest
from sty import RsRegister, Style, Sgr
import renderfunc

@pytest.fixture
def rs_register():
    return RsRegister()

def test_valid_inputs(rs_register):
    assert isinstance(rs_register.all, Style)
    assert isinstance(rs_register.fg, Style)
    assert isinstance(rs_register.bg, Style)
    assert isinstance(rs_register.ef, Style)
    assert isinstance(rs_register.bold_dim, Style)
    assert isinstance(rs_register.dim_bold, Style)
    assert isinstance(rs_register.i, Style)
    assert isinstance(rs_register.italic, Style)
    assert isinstance(rs_register.u, Style)
    assert isinstance(rs_register.underl, Style)
    assert isinstance(rs_register.blink, Style)
    assert isinstance(rs_register.inverse, Style)
    assert isinstance(rs_register.hidden, Style)
    assert isinstance(rs_register.strike, Style)

    # Check that the Sgr numbers are correct for each Style instance
    assert rs_register.all.sgr == [0]
    assert rs_register.fg.sgr == [39]
    assert rs_register.bg.sgr == [49]
    assert rs_register.ef.sgr == [22, 23, 24, 25, 27, 28, 29]
    assert rs_register.bold_dim.sgr == [22]
    assert rs_register.dim_bold.sgr == [22]
    assert rs_register.i.sgr == [23]
    assert rs_register.italic.sgr == [23]
    assert rs_register.u.sgr == [24]
    assert rs_register.underl.sgr == [24]
    assert rs_register.blink.sgr == [25]
    assert rs_register.inverse.sgr == [27]
    assert rs_register.hidden.sgr == [28]
    assert rs_register.strike.sgr == [29]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_RsRegister___init___0_test_valid_inputs
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:4:0: E0401: Unable to import 'renderfunc' (import-error)


"""