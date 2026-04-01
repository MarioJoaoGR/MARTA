
import types
from multiprocessing import pool as mp_pool
from typing import Optional, Callable, Iterable, Any

class DummyPool:
    """
    A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero.

    Parameters:
        processes (Optional[int]): The number of worker processes to use. If set to 0, the pool will use a single-threaded approach. Default is None.
        initializer (Optional[Callable[..., None]]): A callable that will be called at the start of each worker process. It receives any additional arguments passed via ``initargs``. Default is None.
        initargs (Iterable[Any]): Additional arguments to pass to the initializer function. Default is an empty tuple.
        maxtasksperchild (Optional[int]): The maximum number of tasks a child process can execute before being replaced with a new one. If set to 0, there is no limit. Default is None.
        context (Optional[Any]): An optional context object that will be passed to the initializer function and used in the worker processes. Default is None.

    Returns:
        None

    Example:
        To create a DummyPool instance with zero processes, you can use the following code:
        
        ```python
        pool = DummyPool(processes=0)
        ```

        This will initialize a pool that uses single-threaded execution. If you need to pass an initializer function and its arguments, you can do so as follows:

        ```python
        def my_initializer(*args):
            # Your initialization code here
            pass

        pool = DummyPool(processes=0, initializer=my_initializer, initargs=(arg1, arg2))
        ```

    Notes:
        - The ``initializer`` function is called at the start of each worker process. It receives any additional arguments passed via ``initargs``.
        - If ``processes`` is set to 0, the pool will use a single-threaded approach, which can be useful for debugging or when running in an environment with limited resources.
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

        self._state = mp_pool.RUN

    def __getattr__(self, item):
        return types.MethodType(DummyPool._no_op, self)  # no-op for everything else

    @staticmethod
    def _no_op(*args, **kwargs):
        pass

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