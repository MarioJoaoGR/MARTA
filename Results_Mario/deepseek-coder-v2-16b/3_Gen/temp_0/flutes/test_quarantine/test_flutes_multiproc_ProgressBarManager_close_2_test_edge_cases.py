
import pytest
from flutes import ProgressBarManager
import time
import random
from typing import List, Optional, Dict, Any, Iterable, Iterator, Union, Literal
import functools
import multiprocessing as mp

@pytest.fixture(scope="module")
def progress_bar_manager():
    manager = ProgressBarManager()
    yield manager
    # Ensure the progress bar is closed after all tests are done
    manager.close()

def test_progress_bar_creation(progress_bar_manager):
    xs = [1, 2, 3, 4]
    bar = progress_bar_manager.proxy
    assert isinstance(bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}"), Iterator)

def test_progress_bar_update(progress_bar_manager):
    xs = [1, 2, 3, 4]
    bar = progress_bar_manager.proxy
    bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    assert result == sum(xs)

def test_progress_bar_update_with_none(progress_bar_manager):
    xs = [None, None, None]
    bar = progress_bar_manager.proxy
    bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
    result = 0
    for idx, x in enumerate(xs):
        if x is not None:
            result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1 if x is not None else 0, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    assert result == sum([x for x in xs if x is not None])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager_close_2_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_2_test_edge_cases.py:32:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_2_test_edge_cases.py:46:12: E0602: Undefined variable 'flutes' (undefined-variable)

"""