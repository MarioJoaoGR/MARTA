
import multiprocessing as mp
from typing import Callable, Iterable, Optional, Any, Dict

class DummyPool(mp.pool.Pool):
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero."""
    
    def __init__(self, processes: Optional[int] = None, initializer: Optional[Callable[..., None]] = None,
                 initargs: Iterable[Any] = (), maxtasksperchild: Optional[int] = None,
                 context: Optional[Any] = None) -> None:
        super().__init__(processes=processes, initializer=initializer, initargs=initargs, maxtasksperchild=maxtasksperchild, context=context)
        self._process_state = None
        if initializer is not None:
            # A hack to accommodate stateful pools.
            def run_initializer():
                initializer(*initargs)
                return locals()

            self._process_state = run_initializer().get("__state__", None)

        self._state = mp.pool.RUN

    def apply_async(self, fn: Callable[..., Any], args: Iterable[Any] = (), kwds: Dict[str, Any] = {}, *_, **__) -> 'mp.pool.ApplyResult[Any]':
        return DummyApplyResult(self.apply(fn, args, kwds))

class DummyApplyResult(mp.pool.ApplyResult):
    """A result object encapsulating the results of a function call."""
    pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_apply_async_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_apply_async_1_test_edge_cases.py:24:15: E1120: No value for argument 'callback' in constructor call (no-value-for-parameter)
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_apply_async_1_test_edge_cases.py:24:15: E1120: No value for argument 'error_callback' in constructor call (no-value-for-parameter)


"""