
import multiprocessing as mp
from typing import Optional
import pytest

def get_worker_id() -> Optional[int]:
    r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
    proc_name = mp.current_process().name
    if "PoolWorker" in proc_name:
        try:
            worker_id = int(proc_name[(proc_name.find('-') + 1):])
            return worker_id
        except ValueError:
            return None
    return None

@pytest.mark.parametrize("mock_mp, expected", [
    (lambda: {"current_process": lambda: mp.Process(name="PoolWorker-42")}, 42),
    (lambda: {"current_process": lambda: mp.Process(name="PoolWorker-1")}, 1),
    (lambda: {"current_process": lambda: mp.Process(name="PoolWorker-0")}, 0),
    (lambda: {"current_process": lambda: mp.Process(name="OtherName")}, None),
    (lambda: {"current_process": lambda: mp.Process(name="PoolWorker")}, None),
])
def test_get_worker_id(monkeypatch, mock_mp, expected):
    monkeypatch.setattr(mp, "current_process", mock_mp()["current_process"])
    assert get_worker_id() == expected

# Additional test cases to cover uncovered lines 27-31
def test_get_worker_id_invalid_name():
    # Test case where the process name does not contain "PoolWorker"
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(mp, "current_process", lambda: mp.Process(name="NonPoolWorker"))
    assert get_worker_id() is None

def test_get_worker_id_invalid_format():
    # Test case where the process name contains "PoolWorker" but does not follow the expected format
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(mp, "current_process", lambda: mp.Process(name="PoolWorker-fortytwo"))
    assert get_worker_id() is None

def test_get_worker_id_nonexistent_process():
    # Test case where there is no current process (e.g., in a non-multiprocessing context)
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(mp, "current_process", lambda: None)