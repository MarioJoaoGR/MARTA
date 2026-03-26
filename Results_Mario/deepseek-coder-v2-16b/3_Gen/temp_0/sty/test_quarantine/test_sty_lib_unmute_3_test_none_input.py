
import pytest
from sty.lib import Register, unmute

def test_none_input():
    with pytest.raises(ValueError) as excinfo:
        unmute()
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

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

sty/Test4DT_tests/test_sty_lib_unmute_3_test_none_input.py F             [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_lib_unmute_3_test_none_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_lib_unmute_3_test_none_input.py::test_none_input
============================== 1 failed in 0.02s ===============================
"""