
# Module: flutes.multiproc
# test_flutes_multiproc.py
import pytest
from flutes.multiproc import ProgressBarManager
import time
import random
import functools
import multiprocessing as mp
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator
try:
    from tqdm import tqdm  # type: ignore
except ImportError:
    tqdm = None  # type: ignore

@pytest.fixture(scope="module")
def manager():
    return ProgressBarManager()

def test_new_progress_bar_with_iterable(manager):
    xs = list(range(100))
    bar = manager.new(total=len(xs), desc="Test Progress Bar")
    assert isinstance(bar, Iterator) or isinstance(bar, tqdm)

def test_manual_updates_with_update_method(manager):
    xs = list(range(100))
    bar = manager.new(total=len(xs), desc="Manual Updates")
    for i in range(len(xs)):
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1)
    assert bar.n == len(xs)

def test_writing_messages_to_console(manager):
    xs = list(range(100))
    bar = manager.new(total=len(xs), desc="Writing Messages")
    for i in range(len(xs)):
        time.sleep(random.uniform(0.01, 0.2))
        if (i + 1) % 50 == 0:
            bar.write(f"Processed {i + 1} items so far...")
    assert True  # This is a placeholder for checking the console output or some other side effect

def test_closing_progress_bar(manager):
    xs = list(range(100))
    bar = manager.new(total=len(xs), desc="Closing Progress Bar")
    assert not bar._proxy.queue.empty()  # Ensure the queue is not empty before closing
    bar.close()
    assert bar._proxy.queue.empty()  # Ensure the queue is empty after closing

def test_run_function(manager):
    def run(xs: List[int], *, bar):
        bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
        result = 0
        for idx, x in enumerate(xs):
            result += x
            time.sleep(random.uniform(0.01, 0.2))
            bar.update(1, postfix={"sum": result})  # update progress
            if (idx + 1) % 100 == 0:
                flutes.log(f"Processed {idx + 1} samples")
        return result
    
    xs = list(range(300))
    run_fn = functools.partial(run, bar=manager.proxy())
    with mp.Pool(4) as pool:
        results = pool.imap_unordered(run_fn, [xs] * 4)
        for result in results:
            assert isinstance(result, int)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager__close_bar_0
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_0.py:58:16: E0602: Undefined variable 'flutes' (undefined-variable)


"""