
import pytest
from tornado import locks

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locks_BoundedSemaphore___init___0.py F [100%]

=================================== FAILURES ===================================
___________________ test_bounded_semaphore_release_too_many ____________________

    def test_bounded_semaphore_release_too_many():
        sem = locks.BoundedSemaphore(value=2)
        for _ in range(3):
            sem.acquire()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locks_BoundedSemaphore___init___0.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locks_BoundedSemaphore___init___0.py::test_bounded_semaphore_release_too_many
============================== 1 failed in 0.09s ===============================
"""