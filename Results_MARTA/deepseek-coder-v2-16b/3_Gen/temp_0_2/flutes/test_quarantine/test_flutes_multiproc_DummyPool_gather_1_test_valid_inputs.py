
import multiprocessing as mp
from typing import Callable, Iterable, Optional, Any, Iterator, TypeVar

T = TypeVar('T')
R = TypeVar('R')

class DummyPool:
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero.
    
    Parameters:
        processes (Optional[int]): The number of worker processes to use. If set to 0, the pool will use a single thread for execution. Default is None.
        initializer (Optional[Callable[..., None]]): A callable that will be called at the start of each worker process. It can accept any positional and keyword arguments. Default is None.
        initargs (Iterable[Any]): Arguments to pass to the initializer function. Default is an empty tuple.
        maxtasksperchild (Optional[int]): The maximum number of tasks a child process can execute before it is replaced with a new one. If set to 0, the pool will not replace any worker processes. Default is None.
        context (Optional[Any]): An optional context object that can be passed to the initializer function and used in the worker process. Default is None.
    
    Returns:
        Iterator[R]: An iterator that yields results from applying the given function ``fn`` to each item in ``iterable``.
    
    Examples:
        To create a DummyPool instance with 2 processes, you can use:
        ```python
        pool = DummyPool(processes=2)
        ```
        
        To use a single-threaded execution (useful for debugging), set the number of processes to 0:
        ```python
        pool = DummyPool(processes=0)
        ```
        
        You can also provide an initializer function that will be called at the start of each worker process. For example:
        ```python
        def initializer_func(*args):
            print("Initializing worker with args:", args)
        
        pool = DummyPool(processes=2, initializer=initializer_func, initargs=(1, "arg"))
        ```
    
    Note:
        The ``gather`` method is used to apply a function to each item in an iterable and gather the results. It supports additional arguments and keyword arguments that can be passed to the function ``fn``.
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

    def gather(self, fn: Callable[[T], Iterator[R]], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> Iterator[R]:
        if self._process_state is not None:
            locals().update({"__state__": self._process_state})
        for x in iterable:
            yield from fn(x, *args, **kwds)  # type: ignore[call-arg]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.06s =============================
"""