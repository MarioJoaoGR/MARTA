
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

@pytest.fixture(scope="module")
def pool_instance():
    return StatefulPool(Pool, State, (1, 2), (), {'initializer': None})

def test_apply_broadcast(pool_instance):
    def broadcast_fn(state: State) -> int:
        return state.value + 1

    result = pool_instance._apply_broadcast(broadcast_fn, 5)
    assert result is not None
    assert result[0] == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_apply_broadcast ____________________

    @pytest.fixture(scope="module")
    def pool_instance():
>       return StatefulPool(Pool, State, (1, 2), (), {'initializer': None})

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7fc86e283110>
pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7fc86e33c7d0>>
state_class = ~State, state_init_args = (1, 2), args = ()
kwargs = {'initargs': (1, 2), 'initializer': functools.partial(<function _pool_state_init at 0x7fc86dd05300>, ~State)}

    def __init__(self, pool_class: Type['PoolType'], state_class: Type[State], state_init_args: Tuple[Any, ...],
                 args: Tuple[Any, ...], kwargs: Dict[str, Any]):
        self._state_class = state_class
    
        # Store the IDs of all methods of the `PoolState` subclass.
        self._class_methods = set()
        for attr_name in dir(self._state_class):
            attr_val = getattr(self._state_class, attr_name)
            if inspect.isfunction(attr_val):
                self._class_methods.add(id(attr_val))
    
        def get_arg(pos: int, name: str, default=None):
            if len(args) > pos + 1:
                return args[pos]
            if name in kwargs:
                return kwargs[name]
            return default
    
        def set_arg(pos: int, name: str, val):
            nonlocal args
            if len(args) > pos + 1:
                args = args[:pos] + (val,) + args[(pos + 1):]
            else:
                kwargs[name] = val
    
        state_init_fn = functools.partial(_pool_state_init, state_class)
        # If there's a user-defined initializer function...
        initializer = get_arg(1, "initializer", None)
        init_args = get_arg(2, "initargs", ())
        if initializer is not None:
            initializer = functools.partial(_chain_fns, fns=[state_init_fn, initializer])
            init_args = [(state_init_args, {}), (init_args, {})]
        else:
            initializer = state_init_fn
            init_args = state_init_args
        set_arg(1, "initializer", initializer)
        set_arg(2, "initargs", init_args)
    
        self._pool = pool_class(*args, **kwargs)
    
        for name in ["imap", "imap_unordered", "map", "map_async", "starmap", "starmap_async",
                     "apply", "apply_async", "gather"]:
>           pool_method = getattr(self._pool, name)
E           AttributeError: 'Pool' object has no attribute 'gather'

flutes/flutes/multiproc.py:351: AttributeError
---------------------------- Captured stderr setup -----------------------------
Process ForkPoolWorker-1:
Process ForkPoolWorker-2:
Traceback (most recent call last):
Process ForkPoolWorker-3:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-4:
Process ForkPoolWorker-5:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-6:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-7:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-8:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-9:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-10:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-11:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-12:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-13:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-14:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-15:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-16:
Traceback (most recent call last):
Process ForkPoolWorker-17:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-18:
Process ForkPoolWorker-19:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-20:
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-21:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-22:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-23:
Process ForkPoolWorker-24:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-25:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-26:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-27:
Traceback (most recent call last):
Process ForkPoolWorker-28:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-29:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-30:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-31:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-32:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-33:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-34:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-35:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-36:
Traceback (most recent call last):
Process ForkPoolWorker-37:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-38:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-39:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-40:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-41:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-42:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-43:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-44:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-45:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-46:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-47:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-48:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-49:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-50:
Traceback (most recent call last):
Process ForkPoolWorker-51:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-52:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-53:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-54:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-55:
Process ForkPoolWorker-56:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-57:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-58:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-59:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-60:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-61:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-62:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-63:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-64:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-65:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-66:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-67:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-68:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-69:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-70:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-71:
Traceback (most recent call last):
Process ForkPoolWorker-72:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-73:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-74:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-75:
Traceback (most recent call last):
Process ForkPoolWorker-76:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-77:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-78:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-79:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-80:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-81:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-82:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-83:
Traceback (most recent call last):
Process ForkPoolWorker-84:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-85:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-86:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-87:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-88:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-89:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-90:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-91:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-92:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-93:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-94:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-95:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-96:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-97:
Traceback (most recent call last):
Process ForkPoolWorker-98:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-99:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-100:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-101:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-102:
Traceback (most recent call last):
Process ForkPoolWorker-103:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-104:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-105:
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-106:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-107:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-108:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-109:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-110:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-111:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-112:
Traceback (most recent call last):
Process ForkPoolWorker-113:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-114:
Traceback (most recent call last):
Process ForkPoolWorker-115:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-116:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-117:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-118:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-119:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-120:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-121:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-122:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-123:
Process ForkPoolWorker-124:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-125:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-126:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-127:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-128:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_edge_case.py::test_apply_broadcast
=============================== 1 error in 0.67s ===============================

Process ForkPoolWorker-129:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-130:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-131:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-132:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-133:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-134:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-135:
Traceback (most recent call last):
Process ForkPoolWorker-136:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-137:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-138:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-139:
Process ForkPoolWorker-140:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-141:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-142:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-143:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-144:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-145:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-146:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-147:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-148:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-149:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-150:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-151:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-152:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-153:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-154:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-155:
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-156:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-157:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-158:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-159:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-160:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-161:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-162:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-163:
Process ForkPoolWorker-164:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-165:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-166:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-167:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-168:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-169:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-170:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-171:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-172:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-173:
Traceback (most recent call last):
Process ForkPoolWorker-174:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-175:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-176:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-177:
Process ForkPoolWorker-178:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-179:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-180:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-181:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-182:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-183:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-184:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-185:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-186:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-187:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-188:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-189:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-190:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-191:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-192:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-193:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-194:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-195:
Process ForkPoolWorker-196:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-197:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-198:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-199:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-200:
Traceback (most recent call last):
Process ForkPoolWorker-201:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-202:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-203:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-204:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-205:
Traceback (most recent call last):
Process ForkPoolWorker-206:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-207:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-208:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-209:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-210:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-211:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-212:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-213:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-214:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-215:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-216:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-217:
Traceback (most recent call last):
Process ForkPoolWorker-218:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-219:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-220:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-221:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-222:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-223:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-224:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-225:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-226:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-227:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-228:
Traceback (most recent call last):
Process ForkPoolWorker-229:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-230:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-231:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-232:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-233:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-234:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-235:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-236:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-237:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-238:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-239:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-240:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-241:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-242:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-243:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-244:
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-245:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-246:
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-247:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-248:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-249:
Process ForkPoolWorker-250:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-251:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-252:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-253:
Traceback (most recent call last):
Process ForkPoolWorker-254:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-255:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-256:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-257:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-258:
Process ForkPoolWorker-259:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-260:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-261:
Traceback (most recent call last):
Process ForkPoolWorker-262:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-263:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-264:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-265:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-266:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-267:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-268:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-269:
Process ForkPoolWorker-270:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-271:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-272:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-273:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-274:
Traceback (most recent call last):
Process ForkPoolWorker-275:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-276:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-277:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-278:
Traceback (most recent call last):
Process ForkPoolWorker-279:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-280:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-281:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-282:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-283:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-284:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-285:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-286:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-287:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-288:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-289:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-290:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-291:
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-292:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-293:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-294:
Traceback (most recent call last):
Process ForkPoolWorker-295:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-296:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-297:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-298:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-299:
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-300:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-301:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-302:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-303:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-304:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-305:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-306:
Traceback (most recent call last):
Process ForkPoolWorker-307:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-308:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-309:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-310:
Traceback (most recent call last):
Process ForkPoolWorker-311:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-312:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-313:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-314:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-315:
Process ForkPoolWorker-316:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-317:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-318:
Traceback (most recent call last):
Process ForkPoolWorker-319:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-320:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-321:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-322:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-323:
Traceback (most recent call last):
Process ForkPoolWorker-324:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-325:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-326:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-327:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-328:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-329:
Traceback (most recent call last):
Process ForkPoolWorker-330:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-331:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-332:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-333:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-334:
Process ForkPoolWorker-335:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-336:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-337:
Process ForkPoolWorker-338:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-339:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-340:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-341:
Traceback (most recent call last):
Process ForkPoolWorker-342:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-343:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-344:
Process ForkPoolWorker-345:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-346:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-347:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-348:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-349:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-350:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-351:
Process ForkPoolWorker-352:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-353:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-354:
Process ForkPoolWorker-355:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-356:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-357:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-358:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-359:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-360:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-361:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-362:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-363:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-364:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-365:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-366:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-367:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-368:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-369:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-370:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-371:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-372:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-373:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-374:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-375:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-376:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-377:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-378:
Process ForkPoolWorker-379:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-380:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-381:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-382:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-383:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-384:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-385:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-386:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-387:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-388:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-389:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-390:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-391:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-392:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-393:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-394:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-395:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-396:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-397:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-398:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-399:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-400:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-401:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-402:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-403:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-404:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-405:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-406:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-407:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-408:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-409:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-410:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-411:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-412:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-413:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-414:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-416:
Process ForkPoolWorker-415:
Traceback (most recent call last):
Process ForkPoolWorker-417:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-418:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-419:
Process ForkPoolWorker-420:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-421:
Process ForkPoolWorker-422:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-423:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-424:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-425:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-426:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-427:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-428:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-429:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-430:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-431:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-432:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-433:
Traceback (most recent call last):
Process ForkPoolWorker-434:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-435:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-436:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-437:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-438:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-439:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-440:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-441:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-442:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-443:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-444:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-445:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-446:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-447:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-448:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-449:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-450:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-451:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-452:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-453:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-454:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-455:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-456:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-457:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-458:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-459:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-460:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-461:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-462:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-463:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-464:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-465:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-466:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-467:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-468:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-469:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-470:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-471:
Process ForkPoolWorker-472:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-473:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-474:
Process ForkPoolWorker-475:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-476:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-477:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-478:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-479:
Traceback (most recent call last):
Process ForkPoolWorker-480:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-481:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-482:
Traceback (most recent call last):
Process ForkPoolWorker-483:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-484:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-485:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-486:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-487:
Traceback (most recent call last):
Process ForkPoolWorker-488:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-489:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-490:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-491:
Traceback (most recent call last):
Process ForkPoolWorker-492:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-493:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-494:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-495:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-496:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-497:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-498:
Process ForkPoolWorker-499:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-500:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-501:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-502:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-503:
Process ForkPoolWorker-504:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-505:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-506:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-507:
Traceback (most recent call last):
Process ForkPoolWorker-508:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-509:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-510:
Process ForkPoolWorker-511:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-512:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-513:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-514:
Process ForkPoolWorker-515:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-516:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-517:
Process ForkPoolWorker-518:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-519:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-520:
Traceback (most recent call last):
Process ForkPoolWorker-521:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-522:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-523:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-524:
Traceback (most recent call last):
Process ForkPoolWorker-525:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-526:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-527:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-528:
Process ForkPoolWorker-529:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-530:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-531:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-532:
Traceback (most recent call last):
Process ForkPoolWorker-533:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-534:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-535:
Traceback (most recent call last):
Process ForkPoolWorker-536:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-537:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-538:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-539:
Traceback (most recent call last):
Process ForkPoolWorker-540:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-541:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-542:
Traceback (most recent call last):
Process ForkPoolWorker-543:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-544:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-545:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-546:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-547:
Traceback (most recent call last):
Process ForkPoolWorker-548:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-549:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-550:
Process ForkPoolWorker-551:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-552:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-553:
Traceback (most recent call last):
Process ForkPoolWorker-554:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-555:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-556:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-557:
Process ForkPoolWorker-558:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-559:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-560:
Process ForkPoolWorker-561:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-562:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-563:
Traceback (most recent call last):
Process ForkPoolWorker-564:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-565:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-566:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-567:
Process ForkPoolWorker-568:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-569:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-570:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-571:
Traceback (most recent call last):
Process ForkPoolWorker-572:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-573:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-574:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-575:
Process ForkPoolWorker-576:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-577:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-578:
Traceback (most recent call last):
Process ForkPoolWorker-579:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-580:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-581:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-582:
Traceback (most recent call last):
Process ForkPoolWorker-583:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-584:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-585:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-586:
Traceback (most recent call last):
Process ForkPoolWorker-587:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-588:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-589:
Process ForkPoolWorker-590:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-591:
Traceback (most recent call last):
Process ForkPoolWorker-592:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-593:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-594:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-595:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-596:
Traceback (most recent call last):
Process ForkPoolWorker-597:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-598:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-599:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-600:
Process ForkPoolWorker-601:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-602:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-603:
Traceback (most recent call last):
Process ForkPoolWorker-604:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-605:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-606:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-607:
Process ForkPoolWorker-608:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-609:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-610:
Traceback (most recent call last):
Process ForkPoolWorker-611:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-612:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-613:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-614:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-615:
Traceback (most recent call last):
Process ForkPoolWorker-616:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-617:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-618:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-619:
Traceback (most recent call last):
Process ForkPoolWorker-620:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-621:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-622:
Traceback (most recent call last):
Process ForkPoolWorker-623:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-624:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-625:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Process ForkPoolWorker-626:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'TypeVar' object is not callable
Exception ignored in: <function Pool.__del__ at 0x7fc86dd50a40>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 271, in __del__
    self._change_notifier.put(None)
  File "/usr/local/lib/python3.11/multiprocessing/queues.py", line 377, in put
    self._writer.send_bytes(obj)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 427, in _send_bytes
    self._send(header + buf)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 384, in _send
    n = write(self._handle, buf)
        ^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 9] Bad file descriptor
"""