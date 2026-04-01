
import multiprocessing as mp
from typing import Optional, Callable, Iterable, Iterator, Any, TypeVar

T = TypeVar('T')
R = TypeVar('R')

class DummyPool:
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero.
    
    Parameters:
        processes (Optional[int]): The number of worker processes to use. If set to 0, the pool will run in a single-threaded mode. Default is None.
        initializer (Optional[Callable[..., None]]): A callable that will be called at the start of each worker process. It receives ``*initargs`` as arguments. Default is None.
        initargs (Iterable[Any]): Arguments to pass to the initializer function. Default is an empty tuple.
        maxtasksperchild (Optional[int]): The maximum number of tasks a child process can execute before being replaced with a new one. Default is None.
        context (Optional[Any]): An optional context object that will be passed to each worker process. Default is None.
    
    Returns:
        Iterator[R]: An iterator that yields the results of applying the function ``fn`` to each element in ``iterable``.
    
    Examples:
        To use this class, you can create an instance with specific parameters or accept the default values:
        
        >>> pool = DummyPool(processes=0)  # Create a single-threaded pool
        >>> results = list(pool.imap(lambda x: x * 2, [1, 2, 3]))  # Apply a function to an iterable
        >>> print(results)  # Output will be [2, 4, 6]
        
        You can also use the initializer parameter to set up state for each worker process:
        
        >>> def init_worker(state):
        ...     global __state__
        ...     __state__ = state
        ...
        >>> pool = DummyPool(processes=0, initializer=init_worker, initargs=(42,))
        >>> results = list(pool.imap(lambda x: x * __state__, [1, 2, 3]))
        >>> print(results)  # Output will be [42, 84, 126]
    
    Note:
        This class is a wrapper around ``multiprocessing.Pool`` and behaves similarly, but with the ability to run in single-threaded mode when processes are set to zero. The initializer function can be used to initialize state for each worker process.
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

    def imap(self, fn: Callable[[T], R], iterable: Iterable[T], *_, args=(), kwds={}, **__) -> Iterator[R]:
        if self._process_state is not None:
            locals().update({"__state__": self._process_state})
        for x in iterable:
            yield fn(x, *args, **kwds)  # type: ignore[call-arg]

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