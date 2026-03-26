
import multiprocessing as mp
from typing import Callable, Iterable, List, Optional, Any, Mapping

class PoolType:
    """Multiprocessing stateless worker pool. See :class:`StatefulPoolType` for a pool with stateful workers.
    
        .. note::
            This class is only a stub for type annotation and documentation purposes only, and should not be used directly.
            Please refer to :meth:`safe_pool` for a user-facing API for constructing pool instances.
    """
    _state: int
    _processes: int

    def starmap_async(self,  # type: ignore[override]
                       fn: Callable[..., R], iterable: Iterable[Iterable[Any]], chunksize: Optional[int] = None,
                       callback: Optional[Callable[[T], None]] = None,
                       error_callback: Optional[Callable[[BaseException], None]] = None,
                       *, args: Iterable[Any] = (), kwds: Mapping[str, Any] = {}) -> 'mp.pool.ApplyResult[List[R]]':
        r"""Non-blocking version of :meth:`starmap`.
                
                This method submits a list of iterable arguments to the function `fn` in chunks, allowing for non-blocking execution. It returns an ApplyResult object that can be used to check on the progress and results of the computations.
                
                Parameters:
                    fn (Callable[..., R]): The function to apply to each chunk of arguments. This function should accept iterable arguments.
                    iterable (Iterable[Iterable[Any]]): An iterable containing iterables of arguments to pass to `fn`. Each sub-iterable will be passed as a separate argument to `fn`.
                    chunksize (Optional[int]): The size of the chunks into which the input iterable is divided before processing. If not provided, it defaults to an appropriate value based on the number of processes and available memory.
                    callback (Optional[Callable[[T], None]]): An optional callable that will be invoked with the result for each invocation of `fn`. The signature of this callable should match that of its argument type T.
                    error_callback (Optional[Callable[[BaseException], None]]): An optional callable that will be invoked if an exception occurs during the execution of `fn`. The signature of this callable should match that of its argument type BaseException.
                
                Returns:
                    mp.pool.ApplyResult[List[R]]: A result object that can be used to check on the progress and results of the computations.
                
                Example:
                    >>> def multiply(a, b):
                    ...     return a * b
                    ... 
                    >>> pool = PoolType()
                    >>> args_list = [(1, 2), (3, 4), (5, 6)]
                    >>> result = pool.starmap_async(multiply, args_list)
                    >>> # Do other work while the computations are running...
                    >>> results = result.get()  # Retrieve the results when done
        """
        with mp.Pool(self._processes) as pool:
            return pool.starmap_async(fn, iterable, chunksize=chunksize, callback=callback, error_callback=error_callback)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_async_0_test_error_handling
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_error_handling.py:16:41: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_error_handling.py:17:52: E0602: Undefined variable 'T' (undefined-variable)

"""