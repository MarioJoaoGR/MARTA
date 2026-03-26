
# Module: flutes.multiproc
# test_flutes_multiproc.py
import pytest
from flutes.multiproc import ProgressBarManager
import functools
import time
import random
import multiprocessing as mp
from typing import List, Iterable, Dict, Any, Optional, Union, Literal, Iterator, TypeVar

T = TypeVar('T')

def run(xs: List[int], *, bar) -> int:
    # Create a new progress bar for the current worker.
    bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
    # Compute-intensive stuff!
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

def run2(xs: List[int], *, bar) -> int:
    # An alternative way to achieve the same functionalities (though slightly slower):
    result = 0
    for idx, x in enumerate(bar.iter(xs)):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

@pytest.fixture
def manager():
    return ProgressBarManager()

def test_run_function(manager):
    xs = list(range(1000))
    run_fn = functools.partial(run, bar=manager.proxy)
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, [xs] * 4))
        assert all(isinstance(result, int) for result in results)

def test_run2_function(manager):
    xs = list(range(1000))
    run_fn = functools.partial(run2, bar=manager.proxy)
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, [xs] * 4))
        assert all(isinstance(result, int) for result in results)

def test_verbose_false(manager):
    manager = ProgressBarManager(verbose=False)
    run_fn = functools.partial(run, bar=manager.proxy)
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, [[]] * 4))
        assert all(result is None for result in results)

def test_custom_kwargs(manager):
    manager = ProgressBarManager(verbose=True, total=1000, desc="Total Progress")
    run_fn = functools.partial(run, bar=manager.proxy)
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, [list(range(1000))] * 4))
        assert all(isinstance(result, int) for result in results)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager__run_0
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0.py:25:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0.py:37:12: E0602: Undefined variable 'flutes' (undefined-variable)


"""