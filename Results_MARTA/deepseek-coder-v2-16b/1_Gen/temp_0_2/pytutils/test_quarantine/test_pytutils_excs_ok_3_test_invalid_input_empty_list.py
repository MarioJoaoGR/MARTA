
import pytest
from pytutils.excs import ok

def test_invalid_input_empty_list():
    with pytest.raises(ValueError):
        with ok(ValueError):
            # The following line should raise ValueError, but since it's wrapped in the context manager, it won't be raised here.
            pass

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

pytutils/Test4DT_tests/test_pytutils_excs_ok_3_test_invalid_input_empty_list.py F [100%]

=================================== FAILURES ===================================
________________________ test_invalid_input_empty_list _________________________

    def test_invalid_input_empty_list():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_excs_ok_3_test_invalid_input_empty_list.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_excs_ok_3_test_invalid_input_empty_list.py::test_invalid_input_empty_list
============================== 1 failed in 0.05s ===============================
"""