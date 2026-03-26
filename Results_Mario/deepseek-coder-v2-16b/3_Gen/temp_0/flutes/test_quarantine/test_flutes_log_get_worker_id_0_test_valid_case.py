
import pytest
from unittest.mock import patch, Mock
from flutes.log import get_worker_id

@pytest.fixture(autouse=True)
def mock_process():
    with patch('flutes.log.mp.current_process', return_value=Mock(name='PoolWorker-123')):
        yield

def test_valid_case():
    expected_result = 123
    assert get_worker_id() == expected_result

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_get_worker_id_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        expected_result = 123
>       assert get_worker_id() == expected_result

flutes/Test4DT_tests/test_flutes_log_get_worker_id_0_test_valid_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def get_worker_id() -> Optional[int]:
        r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
        proc_name = mp.current_process().name
>       if "PoolWorker" in proc_name:
E       TypeError: argument of type 'Mock' is not iterable

flutes/flutes/log.py:28: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.27s ===============================

"""