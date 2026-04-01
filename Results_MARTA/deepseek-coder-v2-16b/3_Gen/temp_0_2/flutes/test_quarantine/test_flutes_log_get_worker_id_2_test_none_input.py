
import pytest
from unittest.mock import patch
from flutes.log import mp

def get_worker_id() -> Optional[int]:
    r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
    proc_name = mp.current_process().name
    if "PoolWorker" in proc_name:
        worker_id = int(proc_name[(proc_name.find('-') + 1):])
        return worker_id
    return None

@pytest.mark.parametrize("proc_name, expected", [
    ("PoolWorker-123", 123),
    ("OtherName-456", 456),
    ("PoolWorker", None),
    ("PoolWorker-abc", None),
    (None, None)
])
@patch('flutes.log.mp.current_process')
def test_get_worker_id(mock_current_process, proc_name, expected):
    mock_current_process.return_value.name = proc_name
    assert get_worker_id() == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_get_worker_id_2_test_none_input
flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_none_input.py:6:23: E0602: Undefined variable 'Optional' (undefined-variable)


"""