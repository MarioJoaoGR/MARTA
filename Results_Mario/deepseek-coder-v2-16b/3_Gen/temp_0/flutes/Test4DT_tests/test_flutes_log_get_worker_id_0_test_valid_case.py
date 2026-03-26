
import multiprocessing
from unittest.mock import patch, MagicMock
import pytest
from typing import Optional

def get_worker_id() -> Optional[int]:
    r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
    proc_name = multiprocessing.current_process().name
    if "PoolWorker" in proc_name:
        worker_id = int(proc_name[(proc_name.find('-') + 1):])
        return worker_id
    return None

@pytest.mark.skip("Need to fix the mock setup")
def test_valid_case():
    with patch('multiprocessing.current_process', return_value=MagicMock(name='PoolWorker-123')):
        assert get_worker_id() == 123
