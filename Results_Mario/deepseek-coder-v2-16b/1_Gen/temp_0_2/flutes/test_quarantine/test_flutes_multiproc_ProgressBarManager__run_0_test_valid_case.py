
import functools
import multiprocessing as mp
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator, TypeVar, Callable
from tqdm import tqdm
from flutes.multiproc import ProgressBarManager, NewEvent, UpdateEvent, WriteEvent, CloseEvent, QuitEvent

T = TypeVar('T')

def run(xs: List[int], *, bar) -> int:
    """Create a new progress bar for the current worker."""
    bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
    # Compute-intensive stuff!
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    return result

def run2(xs: List[int], *, bar) -> int:
    """An alternative way to achieve the same functionalities (though slightly slower):"""
    result = 0
    for idx, x in enumerate(bar.iter(xs)):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    return result

manager = ProgressBarManager()
# Worker processes interact with the manager through proxies.
run_fn = functools.partial(run, bar=manager.proxy)
with flutes.safe_pool(4) as pool:
    for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
        flutes.log(f"Processed {idx + 1} arrays")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case.py:22:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case.py:33:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case.py:39:5: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case.py:40:56: E0602: Undefined variable 'data' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_case.py:41:8: E0602: Undefined variable 'flutes' (undefined-variable)


"""