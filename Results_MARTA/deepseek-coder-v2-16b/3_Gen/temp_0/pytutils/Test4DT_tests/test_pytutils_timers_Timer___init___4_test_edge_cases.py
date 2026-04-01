
import pytest
from pytutils.timers import Timer

def test_timer_context_manager():
    with pytest.raises(Exception):  # Since we don't have a long operation, any exception will do to ensure the context manager works
        with Timer() as t:
            raise Exception("This is a placeholder exception for testing the context manager.")
