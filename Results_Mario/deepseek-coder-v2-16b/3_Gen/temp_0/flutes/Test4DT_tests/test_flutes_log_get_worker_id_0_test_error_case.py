
import pytest
from unittest.mock import patch
import multiprocessing as mp
from flutes.log import get_worker_id

def test_get_worker_id():
    with patch('multiprocessing.current_process', return_value=mp.Process(name='PoolWorker-123')):
        assert get_worker_id() == 123

    with patch('multiprocessing.current_process', return_value=mp.Process(name='PoolWorker-456')):
        assert get_worker_id() == 456

    with patch('multiprocessing.current_process', return_value=mp.Process(name='OtherName')):
        assert get_worker_id() is None
