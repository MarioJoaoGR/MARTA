
import pytest
from flutes.timing import work_in_progress
import time

def test_valid_case_with_context_manager():
    with pytest.MonkeyPatch.context() as monkeypatch:
        # Mock the time.time function to return a fixed sequence of timestamps
        times = [1672531200 + (i * 0.1) for i in range(10)]
        monkeypatch.setattr(time, 'time', lambda: times.pop(0))
        
        with work_in_progress("Test task"):
            pass
