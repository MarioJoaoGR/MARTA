
import multiprocessing as mp
from typing import Optional, Callable, Iterable, Any

class DummyPool:
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero.
    
    Parameters:
        processes (Optional[int]): The number of worker processes to use. If set to 0, the pool will use a single thread for execution. Default is None.
        initializer (Optional[Callable[..., None]]): A callable that will be called at the start of each worker process. It takes any positional and keyword arguments after ``processes`` as its arguments. Default is None.
        initargs (Iterable[Any]): Positional arguments passed to the initializer function. These are only used if an initializer is provided. Default is an empty tuple.
        maxtasksperchild (Optional[int]): The maximum number of tasks a worker process can execute before terminating and starting a new one. This helps in managing memory usage by periodically restarting workers. Default is None.
        context (Optional[Any]): An optional context object to pass to the pool constructors. It allows customizing aspects of the multiprocessing environment, such as signal handling or forking behavior. Default is None.
    
    Returns:
        None
    
    Examples:
        To create a DummyPool instance with 4 worker processes and an initializer function that sets up some state:
        
        ```python
        def initializer_func(arg1, arg2):
            # Your initialization code here
            pass

        pool = DummyPool(processes=4, initializer=initializer_func, initargs=(arg1, arg2))
        ```
    
        To create a DummyPool instance with single-threaded execution:
        
        ```python
        pool = DummyPool(processes=0)
        ```
    
    Notes:
        - The ``initializer`` function is called at the start of each worker process to set up any necessary state.
        - If ``processes`` is set to 0, the pool will use a single thread for task execution, which can be useful for debugging or when running in an environment with limited resources.
        - The ``context`` parameter allows customizing the multiprocessing environment, providing flexibility based on specific requirements.
    """
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
============================ no tests ran in 0.04s =============================
"""