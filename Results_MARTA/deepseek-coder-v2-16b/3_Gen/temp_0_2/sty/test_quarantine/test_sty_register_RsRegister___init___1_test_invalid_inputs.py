
import pytest
from sty import register

def test_invalid_inputs():
    rs = register.RsRegister()
    
    # Test invalid foreground color
    with pytest.raises(ValueError):
        rs.fg = "invalid_color"  # This should raise a ValueError

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

sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        rs = register.RsRegister()
    
        # Test invalid foreground color
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_register_RsRegister___init___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""