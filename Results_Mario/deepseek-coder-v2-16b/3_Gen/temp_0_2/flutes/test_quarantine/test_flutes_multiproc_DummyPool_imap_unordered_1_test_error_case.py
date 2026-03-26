
import pytest
from flutes.multiproc import DummyPool

def test_error_case():
    pool = DummyPool(processes=0)
    with pytest.raises(ValueError):
        # This should raise a ValueError because the default initializer does not handle any specific arguments
        pool.imap_unordered(lambda x: x * 2, [1, 2, 3])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        pool = DummyPool(processes=0)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_1_test_error_case.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_1_test_error_case.py::test_error_case
============================== 1 failed in 0.09s ===============================
"""