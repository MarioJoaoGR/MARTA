
import pytest
from flutes.multiproc import ProgressBarManager, NewEvent, UpdateEvent, WriteEvent, CloseEvent, QuitEvent
import multiprocessing as mp
import functools
import time
import random
from typing import List, Dict, Optional, Any, Iterable, Union, Literal, Iterator

@pytest.fixture
def manager():
    return ProgressBarManager(verbose=True)

def test_valid_case(manager):
    def run(xs: List[int], *, bar):
        bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
        result = 0
        for idx, x in enumerate(xs):
            result += x
            time.sleep(random.uniform(0.01, 0.2))
            bar.update(1, postfix={"sum": result})
            if (idx + 1) % 100 == 0:
                flutes.log(f"Processed {idx + 1} samples")
        return result
    
    data = [random.randint(1, 100) for _ in range(1000)]
    run_fn = functools.partial(run, bar=manager.proxy)
    
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, data))
        assert len(results) == len(data)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case.py:23:16: E0602: Undefined variable 'flutes' (undefined-variable)


"""