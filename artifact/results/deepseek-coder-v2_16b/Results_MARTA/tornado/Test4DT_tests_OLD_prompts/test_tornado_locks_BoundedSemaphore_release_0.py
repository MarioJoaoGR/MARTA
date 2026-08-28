
import pytest
from unittest.mock import patch, MagicMock
from tornado.locks import BoundedSemaphore


def test_bounded_semaphore_release_too_many():
    with patch('tornado.locks.BoundedSemaphore', autospec=True) as mock_bounded_semaphore:
        # Create a BoundedSemaphore instance with an initial value of 1
        sem = BoundedSemaphore(value=1)
        
        # Call release() once before calling acquire(), which should raise ValueError
        with pytest.raises(ValueError):
            sem.release()