
import multiprocessing
from typing import Callable, Iterator, Optional, TypeVar
from flutes.multiproc import END_SIGNATURE, log_exception

R = TypeVar('R')
T = TypeVar('T')

def _gather_fn(queue: 'mp.Queue[R]', fn: Callable[[T], Iterator[R]], *args, **kwargs) -> Optional[bool]:
    try:
        for x in fn(*args, **kwargs):  # type: ignore[call-arg]
            queue.put(x)
    except Exception as e:
        log_exception(e)
    # No matter what happens, signal the end of generation.
    queue.put(cast(R, END_SIGNATURE))
    return True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__gather_fn_3_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc__gather_fn_3_test_edge_cases.py:16:14: E0602: Undefined variable 'cast' (undefined-variable)


"""