
import multiprocessing
from unittest.mock import patch, MagicMock
from flutes.log import get_worker_id

def test_error_case():
    with patch('multiprocessing.current_process', return_value=MagicMock(name='PoolWorker-123')):
        assert get_worker_id() == 123

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

flutes/Test4DT_tests/test_flutes_log_get_worker_id_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with patch('multiprocessing.current_process', return_value=MagicMock(name='PoolWorker-123')):
>           assert get_worker_id() == 123
E           assert None == 123
E            +  where None = get_worker_id()

flutes/Test4DT_tests/test_flutes_log_get_worker_id_1_test_error_case.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_1_test_error_case.py::test_error_case
============================== 1 failed in 0.10s ===============================
"""