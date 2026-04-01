
import pytest
from sty import Style, Sgr, renderfunc
from sty.register import RsRegister

def test_sty_register_RsRegister___init__():
    rs = RsRegister()
    
    assert isinstance(rs.all, Style)
    assert isinstance(rs.fg, Style)
    assert isinstance(rs.bg, Style)
    assert isinstance(rs.ef, Style)
    assert isinstance(rs.bold_dim, Style)
    assert isinstance(rs.dim_bold, Style)
    assert isinstance(rs.i, Style)
    assert isinstance(rs.italic, Style)
    assert isinstance(rs.u, Style)
    assert isinstance(rs.underl, Style)
    assert isinstance(rs.blink, Style)
    assert isinstance(rs.inverse, Style)
    assert isinstance(rs.hidden, Style)
    assert isinstance(rs.strike, Style)
    
    # Check that the SGR numbers are correct for each style
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
************* Module Test4DT_tests.test_sty_register_RsRegister___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:25:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:26:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:27:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:28:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:29:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:30:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:31:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:32:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:33:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:34:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:35:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:36:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:37:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:38:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)


"""