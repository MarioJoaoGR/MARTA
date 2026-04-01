
import multiprocessing as mp
from typing import Optional, Callable, Iterable, Any, Iterator

class DummyPool:
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero.
    
    Parameters:
        processes (Optional[int]): The number of worker processes to use. If set to 0, the pool will use a single thread for execution. Default is None.
        initializer (Optional[Callable[..., None]]): A callable that will be called at the start of each worker process. It takes any arguments passed in ``initargs`` as its parameters. Default is None.
        initargs (Iterable[Any]): An iterable of arguments to pass to the initializer function. Default is an empty tuple.
        maxtasksperchild (Optional[int]): The maximum number of tasks a worker process can execute before being replaced with a new one. If set to 0, workers will not be replaced. Default is None.
        context (Optional[Any]): An optional context object that will be passed to the initializer function and used in the pool. Default is None.
    
    Returns:
        None
    
    Examples:
        To create a DummyPool instance with no additional initialization or specific task limits, you can use:
        
        >>> from multiprocessing import Pool
        >>> dummy_pool = DummyPool(processes=0)
        
        If you need to initialize each worker process with a custom function and arguments, you can do so by providing the initializer and initargs parameters:
        
        >>> def initializer_func():
        ...     print("Initializing worker")
        ... 
        >>> dummy_pool = DummyPool(processes=0, initializer=initializer_func)
        
        This will call `initializer_func()` at the start of each worker process and output "Initializing worker" to the console.
    
    Notes:
        The ``DummyPool`` class is a wrapper around ``multiprocessing.Pool`` that overrides the default behavior when the number of processes is set to 0, using single-threaded execution instead. This can be useful for debugging or running tasks in a controlled environment where parallelism is not desired.
    """
    def __init__(self, processes: Optional[int] = None, initializer: Optional[Callable[..., None]] = None,
                 initargs: Iterable[Any] = (), maxtasksperchild: Optional[int] = None,
                 context: Optional[Any] = None) -> None:
        self._process_state = None
        if initializer is not None:
            # A hack to accommodate stateful pools.
            def run_initializer():
                initializer(*initargs)
                return locals()

            self._process_state = run_initializer().get("__state__", None)

        self._state = mp.pool.RUN  # Correctly assign the RUN attribute from multiprocessing.pool

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
============================ no tests ran in 0.05s =============================
"""