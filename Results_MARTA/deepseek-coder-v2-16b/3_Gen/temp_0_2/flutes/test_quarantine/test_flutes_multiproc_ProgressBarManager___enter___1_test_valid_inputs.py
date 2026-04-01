
import pytest
from flutes.multiproc import ProgressBarManager
import time
import random
from typing import List, Iterable, Dict, Any, Optional, Union, Literal, Iterator, overload

@pytest.fixture(scope="module")
def progress_bar_manager():
    manager = ProgressBarManager(verbose=True)
    yield manager
    # Ensure the thread is joined after all tests are done
    if hasattr(manager, 'thread') and manager.thread.is_alive():
        manager.thread.join()

def test_valid_inputs(progress_bar_manager):
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
    
    def run2(xs: List[int], *, bar):
        result = 0
        for idx, x in enumerate(bar.iter(xs)):
            result += x
            time.sleep(random.uniform(0.01, 0.2))
            bar.update(postfix={"sum": result})
            if (idx + 1) % 100 == 0:
                flutes.log(f"Processed {idx + 1} samples")
        return result
    
    manager = progress_bar_manager
    run_fn = lambda xs: run(xs, bar=manager.proxy)
    with flutes.safe_pool(4) as pool:
        data = [[random.randint(1, 100) for _ in range(1000)] for _ in range(5)]
        results = list(pool.imap_unordered(run_fn, data))
        assert len(results) == len(data), "Number of results does not match number of input lists"
        for result in results:
            assert isinstance(result, int), "Result is not an integer"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs.py:25:16: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs.py:35:16: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_valid_inputs.py:40:9: E0602: Undefined variable 'flutes' (undefined-variable)


"""