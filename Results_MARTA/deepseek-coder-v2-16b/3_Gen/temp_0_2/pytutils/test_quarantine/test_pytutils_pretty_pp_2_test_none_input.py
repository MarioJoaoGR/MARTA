
import pytest
from pytutils.pretty import pp

def test_none_input():
    with pytest.raises(TypeError):
        pp(None)  # Since the function expects a valid argument, we expect a TypeError if none is provided

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_pretty_pp_2_test_none_input.py F    [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_pretty_pp_2_test_none_input.py:6: Failed
----------------------------- Captured stdout call -----------------------------
[38;2;102;217;239mNone[39m
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_pretty_pp_2_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""