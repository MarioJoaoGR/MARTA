
import pytest
import functools
import multiprocessing as mp
from typing import List, Iterable, Dict, Optional, Any, Union, Literal, Iterator
from collections import defaultdict
import time
import random
import threading
from flutes.multiproc import ProgressBarManager

def run(xs: List[int], *, bar):
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

def run2(xs: List[int], *, bar):
    # An alternative way to achieve the same functionalities (though slightly slower):
    result = 0
    for idx, x in enumerate(bar.iter(xs)):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

@pytest.fixture
def manager():
    manager = ProgressBarManager()
    yield manager
    manager.close()

def test_valid_inputs(manager):
    data = [[i for i in range(100)] for _ in range(4)]
    
    run_fn = functools.partial(run, bar=manager.proxy())
    with flutes.safe_pool(4) as pool:
        for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
            flutes.log(f"Processed {idx + 1} arrays")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager_proxy_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_valid_inputs.py:23:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_valid_inputs.py:35:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_valid_inputs.py:48:9: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_valid_inputs.py:50:12: E0602: Undefined variable 'flutes' (undefined-variable)


"""