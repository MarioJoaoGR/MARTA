
import pytest
from sty import register

def test_valid_inputs():
    rs = register.RsRegister()
    
    # Check that each attribute is properly initialized
    assert isinstance(rs.all, register.Style)
    assert isinstance(rs.fg, register.Style)
    assert isinstance(rs.bg, register.Style)
    assert isinstance(rs.ef, register.Style)
    assert isinstance(rs.bold_dim, register.Style)
    assert isinstance(rs.dim_bold, register.Style)
    assert isinstance(rs.i, register.Style)
    assert isinstance(rs.italic, register.Style)
    assert isinstance(rs.u, register.Style)
    assert isinstance(rs.underl, register.Style)
    assert isinstance(rs.blink, register.Style)
    assert isinstance(rs.inverse, register.Style)
    assert isinstance(rs.hidden, register.Style)
    assert isinstance(rs.strike, register.Style)
    
    # Check that the SGR numbers are correct for each attribute
    assert rs.all.sgr == [0]
    assert rs.fg.sgr == [39]
    assert rs.bg.sgr == [49]
    assert rs.ef.sgr == [22, 23, 24, 25, 27, 28, 29]
    assert rs.bold_dim.sgr == [22]
    assert rs.dim_bold.sgr == [22]
    assert rs.i.sgr == [23]
    assert rs.italic.sgr == [23]
    assert rs.u.sgr == [24]
    assert rs.underl.sgr == [24]
    assert rs.blink.sgr == [25]
    assert rs.inverse.sgr == [27]
    assert rs.hidden.sgr == [28]
    assert rs.strike.sgr == [29]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_RsRegister___init___0_test_valid_inputs
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:25:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:26:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:27:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:28:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:29:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:30:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:31:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:32:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:33:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:34:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:35:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:36:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:37:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:38:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)

"""