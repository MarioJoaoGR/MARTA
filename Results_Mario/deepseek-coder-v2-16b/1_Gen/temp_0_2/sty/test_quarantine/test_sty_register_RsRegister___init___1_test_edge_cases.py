
import pytest
from sty import register

def test_edge_cases():
    rs = register.RsRegister()
    
    # Test with None values
    assert rs.all is not None
    assert rs.fg is not None
    assert rs.bg is not None
    assert rs.ef is not None
    assert rs.bold_dim is not None
    assert rs.dim_bold is not None
    assert rs.i is not None
    assert rs.italic is not None
    assert rs.u is not None
    assert rs.underl is not None
    assert rs.blink is not None
    assert rs.inverse is not None
    assert rs.hidden is not None
    assert rs.strike is not None
    
    # Test with empty values (should be same as default)
    assert rs.all == register.Style(register.Sgr(0))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        rs = register.RsRegister()
    
        # Test with None values
        assert rs.all is not None
        assert rs.fg is not None
        assert rs.bg is not None
        assert rs.ef is not None
        assert rs.bold_dim is not None
        assert rs.dim_bold is not None
        assert rs.i is not None
        assert rs.italic is not None
        assert rs.u is not None
        assert rs.underl is not None
        assert rs.blink is not None
        assert rs.inverse is not None
        assert rs.hidden is not None
        assert rs.strike is not None
    
        # Test with empty values (should be same as default)
>       assert rs.all == register.Style(register.Sgr(0))
E       AssertionError: assert '\x1b[0m' == ''
E         
E         + [0m

sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================
"""