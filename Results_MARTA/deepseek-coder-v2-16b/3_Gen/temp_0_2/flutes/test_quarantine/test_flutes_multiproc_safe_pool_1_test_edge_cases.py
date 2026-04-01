
import contextlib
from multiprocessing import Pool, DummyPool
from flutes.multiproc import StatefulPool, PoolState

def safe_pool(processes, *args, state_class=None, init_args=(), closing=None, suppress_exceptions=False, **kwargs):
    """
    A wrapper over :py:class:`multiprocessing.Pool <multiprocessing.pool.Pool>` with additional functionalities:
    
    - Fallback to sequential execution when ``processes == 0``.
    - Stateful processes: Functions run in the pool will have access to a mutable state class. See :class:`PoolState` for details.
    - Handles exceptions gracefully.
    - All pool methods support ``args`` and ``kwds``, which allows passing arguments to the called function.
    
    Please see :class:`PoolType` (non-stateful) and :class:`StatefulPoolType` for supported methods of the pool instance.

    :param processes: The number of worker processes to run. A value of 0 means sequential execution in the current process.
    :param state_class: The class of the pool state. This allows functions run by the pool to access a mutable process-local state. The ``state_class`` must be a subclass of :class:`PoolState`. Defaults to None.
    :param init_args: Arguments to the initializer of the pool state. The state will be constructed with:
        .. code:: python
            state = state_class(*init_args)
    :param closing: An optional list of objects to close at exit, routines to run at exit. For each element ``obj``:
        - If it is a context manager (object with an ``__exit__`` method), the ``__exit__`` method is called with appropriate arguments.
        - If it has a ``close()`` method, ``obj.close()`` is invoked.
        - If it is a callable, ``obj`` is called with no arguments.
        - Otherwise, an exception is raised before the pool is constructed.
    :param suppress_exceptions: If True, exceptions raised within the lifetime of the pool are suppressed. Defaults to False.
    :return: A context manager that can be used in a ``with`` statement.
    
    Example usage:
    
    .. code-block:: python
    
        from multiprocessing import Pool
        
        def square(x):
            return x * x
        
        with safe_pool(processes=4) as pool:
            results = pool.map(square, range(10))
            print(results)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    if state_class is not None:
        if not issubclass(state_class, PoolState) or state_class is PoolState:
            raise ValueError("`state_class` must be a subclass of `flutes.PoolState`")

    if closing is not None and not isinstance(closing, list):
        raise ValueError("`closing` should either be `None` or a list")

    with contextlib.ExitStack() as exit_stack:
        for obj in (closing or []):
            if hasattr(obj, "__exit__") and callable(getattr(obj, "__exit__")):
                exit_stack.push(obj.__exit__)
            elif hasattr(obj, "close") and callable(getattr(obj, "close")):
                exit_stack.enter_context(contextlib.closing(obj))
            elif callable(obj):
                exit_stack.callback(obj)
            else:
                raise ValueError("Invalid object in `closing` list. "
                                 "The object must either be a callable or has a `close` method")

        if processes == 0:
            pool_class = DummyPool
        else:
            pool_class = PoolWrapper

        args = (processes,) + args
        if state_class is not None:
            pool = StatefulPool(pool_class, state_class, init_args, args, kwargs)
        else:
            pool = pool_class(*args, **kwargs)

        if processes == 0:
            # Don't swallow exceptions in the single-process case.
            yield pool
            return

        try:
            yield pool
        except KeyboardInterrupt as e:
            from .log import log  # prevent circular import
            log("Gracefully shutting down...", "warning", force_console=True)
            log("Press Ctrl-C again to force terminate...", force_console=True, timestamp=False)
            try:
                pool.close()
                pool.join()
            except KeyboardInterrupt:
                pass
            raise e  # keyboard interrupts are always reraised
        except Exception as e:
            if suppress_exceptions:
                from .log import log  # prevent circular import
                log(traceback.format_exc(), force_console=True, timestamp=False)
            else:
                raise e
        finally:
            # In Python 3.8, the interpreter hangs when the pool is not properly closed.
            pool.close()
            pool.terminate()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_cases.py:3:0: E0611: No name 'DummyPool' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_cases.py:65:25: E0602: Undefined variable 'PoolWrapper' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_cases.py:81:12: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_cases.py:92:16: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_cases.py:93:20: E1101: Class 'traceback' has no 'format_exc' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_cases.py:93:20: E0602: Undefined variable 'traceback' (undefined-variable)


"""