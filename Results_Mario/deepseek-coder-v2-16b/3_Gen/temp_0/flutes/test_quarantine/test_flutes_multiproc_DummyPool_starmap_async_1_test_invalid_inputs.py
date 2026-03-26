
import pytest
from multiprocessing import Pool, pool
from typing import Callable, Iterable, List, Tuple, Any, Optional

class DummyPool(Pool):
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero."""
    
    def __init__(self, processes: Optional[int] = None, initializer: Optional[Callable[..., None]] = None,
                 initargs: Iterable[Any] = (), maxtasksperchild: Optional[int] = None, context: Optional[Any] = None) -> None:
        super().__init__(processes=processes, initializer=initializer, initargs=initargs, maxtasksperchild=maxtasksperchild, context=context)
        self._process_state = None
        if initializer is not None:
            # A hack to accommodate stateful pools.
            def run_initializer():
                initializer(*initargs)
                return locals()

            self._process_state = run_initializer().get("__state__", None)

        self._state = pool.RUN

    def starmap_async(self, fn: Callable[..., R], iterable: Iterable[Tuple[T, ...]], *_, args=(), kwds={}, **__) \
            -> 'mp.pool.ApplyResult[List[R]]':
        return DummyApplyResult(self.starmap(fn, iterable, args=args, kwds=kwds))

class DummyApplyResult:
    def __init__(self, result):
        self._result = result

    def get(self, *args, **kwargs):
        return self._result

@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_invalid_inputs(dummy_pool):
    with pytest.raises(TypeError):
        # Test invalid function type
        dummy_pool.starmap_async(lambda x, y: x + y, [(1,)], args=(1,))
        
    with pytest.raises(ValueError):
        # Test invalid iterable type
        dummy_pool.starmap_async(lambda x, y: x + y, [1])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_starmap_async_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_async_1_test_invalid_inputs.py:6:0: E0239: Inheriting 'Pool', which is not a class. (inherit-non-class)
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_async_1_test_invalid_inputs.py:23:46: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_async_1_test_invalid_inputs.py:23:75: E0602: Undefined variable 'T' (undefined-variable)

"""