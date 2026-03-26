
import pytest
from codetiming import Timer
from unittest.mock import patch, MagicMock

def test_stop_valid_input():
    timer = Timer()
    with patch('time.perf_counter', return_value=10):
        timer.start()
        with patch('time.perf_counter', return_value=20):
            elapsed_time = timer.stop()
            assert elapsed_time == 10
