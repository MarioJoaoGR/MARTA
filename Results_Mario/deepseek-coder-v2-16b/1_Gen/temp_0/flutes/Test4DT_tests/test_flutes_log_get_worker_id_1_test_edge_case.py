
import multiprocessing as mp
from unittest.mock import patch, Mock
import pytest
from typing import Optional

def get_worker_id() -> Optional[int]:
    r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
    proc_name = mp.current_process().name
    if "PoolWorker" in proc_name:
        worker_id = int(proc_name[(proc_name.find('-') + 1):])
        return worker_id
    return None

@pytest.mark.skip(reason="This test is for demonstration purposes and should be run manually.")
def test_edge_case():
    with patch('multiprocessing.current_process', return_value=Mock(name='Process-1')):
        assert get_worker_id() is None
