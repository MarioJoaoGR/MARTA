
import functools
import multiprocessing as mp
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator, TypeVar
from collections import defaultdict
import threading
from flutes.multiproc import ProgressBarManager

T = TypeVar('T')

def run(xs: List[int], *, bar) -> int:
    # Create a new progress bar for the current worker.
    if isinstance(bar, ProgressBarManager.Proxy):
        bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
    else:
        raise TypeError("Expected an instance of ProgressBarManager.Proxy")
    
    # Compute-intensive stuff!
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        if isinstance(bar, ProgressBarManager.Proxy):
            bar.update(1, postfix={"sum": result})  # update progress
        else:
            raise TypeError("Expected an instance of ProgressBarManager.Proxy")
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

def run2(xs: List[int], *, bar) -> int:
    # An alternative way to achieve the same functionalities (though slightly slower):
    if isinstance(bar, ProgressBarManager.Proxy):
        iterator = bar.iter(xs)
    else:
        raise TypeError("Expected an instance of ProgressBarManager.Proxy")
    
    result = 0
    for idx, x in enumerate(iterator):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        if isinstance(bar, ProgressBarManager.Proxy):
            bar.update(postfix={"sum": result})  # update progress
        else:
            raise TypeError("Expected an instance of ProgressBarManager.Proxy")
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

manager = flutes.ProgressBarManager()
# Worker processes interact with the manager through proxies.
run_fn = functools.partial(run, bar=manager.proxy)
with flutes.safe_pool(4) as pool:
    for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
        flutes.log(f"Processed {idx + 1} arrays")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:31:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:51:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:54:10: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:57:5: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:58:56: E0602: Undefined variable 'data' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:59:8: E0602: Undefined variable 'flutes' (undefined-variable)


"""