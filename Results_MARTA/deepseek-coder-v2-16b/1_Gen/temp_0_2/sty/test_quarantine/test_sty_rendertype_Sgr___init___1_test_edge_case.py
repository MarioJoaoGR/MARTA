
import pytest
from sty import rendertype

def test_edge_case():
    sgr = Sgr(0)
    assert sgr.args == [0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_rendertype_Sgr___init___1_test_edge_case
sty/Test4DT_tests/test_sty_rendertype_Sgr___init___1_test_edge_case.py:6:10: E0602: Undefined variable 'Sgr' (undefined-variable)


"""