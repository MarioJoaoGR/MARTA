
import pytest
from unittest.mock import patch, MagicMock
from tornado.locks import BoundedSemaphore


def test_bounded_semaphore_acquire():
    with patch('tornado.locks.BoundedSemaphore', autospec=True) as mock_sema:
        sema = BoundedSemaphore(value=2)
    
        # Test acquire when there are available permits
        for _ in range(2):
            sema.acquire()
        assert sema._value == 0
