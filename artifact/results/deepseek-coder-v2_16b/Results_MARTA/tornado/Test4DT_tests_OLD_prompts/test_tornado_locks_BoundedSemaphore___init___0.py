
import pytest
from unittest.mock import patch
from tornado.locks import BoundedSemaphore

def test_bounded_semaphore_release():
    sem = BoundedSemaphore(value=2)
    with pytest.raises(ValueError):
        for _ in range(3):
            sem.release()
