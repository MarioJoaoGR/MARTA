
import pytest
from tornado import locks


def test_bounded_semaphore_release_within_limit():
    sem = locks.BoundedSemaphore(value=2)
    for _ in range(2):
        sem.acquire()
    try:
        sem.release()
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError raised: {e}")