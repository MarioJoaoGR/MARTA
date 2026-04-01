
import pytest
from flutes.multiproc import ProgressBarManager
import time
import random
from typing import List, Optional, Dict, Any, Iterable, Iterator, Union, Literal
import functools
import multiprocessing as mp
import threading
from collections import defaultdict

class TestProgressBarManager:
    @pytest.fixture(scope="function")
    def progress_bar_manager(self):
        manager = ProgressBarManager()
        yield manager
        # Ensure the thread is joined after the test
        if hasattr(manager, 'thread') and manager.thread.is_alive():
            manager.thread.join()

    @pytest.mark.parametrize("update_frequency", [1, 0.1])
    def test_valid_inputs(self, progress_bar_manager, update_frequency):
        xs = list(range(100))
        result = progress_bar_manager._proxy.new(xs, update_frequency=update_frequency)
        
        assert isinstance(result, Iterator), "Expected an iterator from the new method"
        
        expected_total = len(xs) if isinstance(update_frequency, int) else None
        for idx, x in enumerate(result):
            time.sleep(random.uniform(0.01, 0.2))
            progress_bar_manager._proxy.update(1)
            if (idx + 1) % (expected_total // 10 if expected_total else 10) == 0:
                assert progress_bar_manager.progress_bars[None].n == idx + 1, f"Expected update to be {idx + 1}, but got {progress_bar_manager.progress_bars[None].n}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""