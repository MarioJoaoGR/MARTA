
import pytest
from sty import renderfunc

def test_invalid_input():
    # Test with a string (should raise an error)
    with pytest.raises(ValueError):
        renderfunc.eightbit_bg("invalid")

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

sty/Test4DT_tests/test_sty_renderfunc_eightbit_bg_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with a string (should raise an error)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_renderfunc_eightbit_bg_2_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_eightbit_bg_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""