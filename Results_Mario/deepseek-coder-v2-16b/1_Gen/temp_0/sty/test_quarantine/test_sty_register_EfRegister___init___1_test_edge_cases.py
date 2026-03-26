
import pytest
from sty import Style, Sgr, renderfunc
from sty.register import EfRegister

def test_ef_register_init():
    ef_register = EfRegister()
    assert hasattr(ef_register, 'b')
    assert isinstance(ef_register.b, Style)
    assert ef_register.b.sgr == Sgr(1)
    assert ef_register.bold.sgr == Sgr(1)
    assert ef_register.dim.sgr == Sgr(2)
    assert ef_register.i.sgr == Sgr(3)
    assert ef_register.italic.sgr == Sgr(3)
    assert ef_register.u.sgr == Sgr(4)
    assert ef_register.underl.sgr == Sgr(4)
    assert ef_register.blink.sgr == Sgr(5)
    assert ef_register.inverse.sgr == Sgr(7)
    assert ef_register.hidden.sgr == Sgr(8)
    assert ef_register.strike.sgr == Sgr(9)
    assert isinstance(ef_register.rs, Style)
    assert len(ef_register.rs.sgr) == 7 and all(isinstance(sgr, int) for sgr in ef_register.rs.sgr)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_EfRegister___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:10:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:11:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:12:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:13:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:14:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:15:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:16:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:17:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:18:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:19:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:20:11: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:22:15: E1101: Instance of 'Style' has no 'sgr' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___1_test_edge_cases.py:22:80: E1101: Instance of 'Style' has no 'sgr' member (no-member)

"""