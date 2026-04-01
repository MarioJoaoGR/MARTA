
import multiprocessing as mp
from unittest.mock import patch
import pytest
from typing import Optional

def get_worker_id() -> Optional[int]:
    r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
    proc_name = mp.current_process().name
    if "PoolWorker" in proc_name:
        worker_id = int(proc_name[(proc_name.find('-') + 1):])
        return worker_id
    return None

@pytest.fixture(autouse=True)
def mock_poolworker():
    with patch('multiprocessing.current_process', return_value=mp.Process(target=None, name='PoolWorker-1')):
        yield

def test_valid_input():
    assert get_worker_id() == 1
