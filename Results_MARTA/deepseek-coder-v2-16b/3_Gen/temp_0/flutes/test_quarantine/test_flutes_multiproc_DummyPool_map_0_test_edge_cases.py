
import pytest
from multiprocessing import Pool, Manager
from typing import Callable, Iterable, List, Optional, Any, TypeVar
import flutes.multiproc as mp

T = TypeVar('T')
R = TypeVar('R')

class DummyPool:
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero.
    
    This implementation provides a flexible interface for mapping an asynchronous function over a list of items in parallel, leveraging Python's multiprocessing module to execute tasks concurrently. When the number of processes is set to 0, it defaults to using a single thread for execution, which can be useful for scenarios where the overhead of creating multiple processes is undesirable or unnecessary.
    
    Parameters:
        processes (Optional[int]): The number of worker processes to use. If set to 0, the pool will use a single thread for execution. Default is None.
        initializer (Optional[Callable[..., None]]): A callable that will be called at the start of each worker process. It receives ``*initargs`` as arguments. Default is None.
        initargs (Iterable[Any]): Arguments to pass to the initializer function. Default is an empty tuple.
        maxtasksperchild (Optional[int]): The maximum number of tasks a child process can execute before being replaced with a new one. Default is None.
        context (Optional[Any]): An optional context object that will be passed to each worker process. Default is None.
    
    Returns:
        List[R]: A list containing the results of applying the function ``fn`` to each element in ``iterable``.
    
    Examples:
        To create a DummyPool instance with 0 processes and an initializer function::
        
            def initializer_func(arg1, arg2):
                # Your initialization code here
                pass
            
            pool = DummyPool(processes=0, initializer=initializer_func, initargs=(arg1, arg2))
        
        To use the ``map`` method of the DummyPool instance to apply a function to an iterable::
        
            def my_function(x):
                return x * 2
            
            results = pool.map(my_function, range(5))
            for result in results:
                print(result)
    """
    _state: int
    def __init__(self, processes: Optional[int] = None, initializer: Optional[Callable[..., None]] = None,
                 initargs: Iterable[Any] = (), maxtasksperchild: Optional[int] = None,
                 context: Optional[Any] = None) -> None:
        self._process_state = None
        if initializer is not None:
            # A hack to accomodate stateful pools.
            def run_initializer():
                initializer(*initargs)
                return locals()

            self._process_state = run_initializer().get("__state__", None)

        self._state = mp.pool.RUN

    def map(self, fn: Callable[[T], R], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> List[R]:
        with Manager() as manager:
            result_list = manager.list()
            with mp.Pool(processes=0 if self._state == mp.pool.RUN else None) as pool:
                for item in iterable:
                    pool.apply_async(fn, (item,) + args, kwds={**kwds, "_result_list": result_list}, callback=lambda _: None)
                pool.close()
                pool.join()
        return list(result_list)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_map_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_0_test_edge_cases.py:56:22: E1101: Module 'flutes.multiproc' has no 'pool' member; maybe 'Pool'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_0_test_edge_cases.py:61:55: E1101: Module 'flutes.multiproc' has no 'pool' member; maybe 'Pool'? (no-member)


"""