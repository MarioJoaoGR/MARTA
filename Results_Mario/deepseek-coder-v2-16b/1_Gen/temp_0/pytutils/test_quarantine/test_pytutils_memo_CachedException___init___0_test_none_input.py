
from pytutils.memo import CachedException
import pytest

def test_none_input():
    # Test when ex is None
    cached_exception = None  # Assigning None to simulate no input
    with pytest.raises(TypeError):
        CachedException(cached_exception)

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

pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Test when ex is None
        cached_exception = None  # Assigning None to simulate no input
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___0_test_none_input.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___0_test_none_input.py::test_none_input
============================== 1 failed in 0.05s ===============================
"""