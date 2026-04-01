
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

def test_invalid_inputs():
    # Test that initializing StatefulPool with None as pool_class raises a TypeError
    with pytest.raises(TypeError):
        StatefulPool(None, State, (), (), {})

    # Test that initializing StatefulPool with an invalid type for pool_class raises a TypeError
    with pytest.raises(TypeError):
        StatefulPool("invalid_type", State, (), (), {})

    # Test that initializing StatefulPool with None as state_class raises a TypeError
    with pytest.raises(TypeError):
        StatefulPool(Pool, None, (), (), {})

    # Test that initializing StatefulPool with an invalid type for state_class raises a TypeError
    with pytest.raises(TypeError):
        StatefulPool(Pool, "invalid_type", (), (), {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test that initializing StatefulPool with None as pool_class raises a TypeError
        with pytest.raises(TypeError):
            StatefulPool(None, State, (), (), {})
    
        # Test that initializing StatefulPool with an invalid type for pool_class raises a TypeError
        with pytest.raises(TypeError):
            StatefulPool("invalid_type", State, (), (), {})
    
        # Test that initializing StatefulPool with None as state_class raises a TypeError
        with pytest.raises(TypeError):
>           StatefulPool(Pool, None, (), (), {})

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7ff092e2c050>
pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7ff091cf1690>>
state_class = None, state_init_args = (), args = ()
kwargs = {'initargs': (), 'initializer': functools.partial(<function _pool_state_init at 0x7ff091c4ba60>, None)}

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
----------------------------- Captured stderr call -----------------------------
Process ForkPoolWorker-1:
Process ForkPoolWorker-2:
Process ForkPoolWorker-3:
Traceback (most recent call last):
Process ForkPoolWorker-4:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-6:
Traceback (most recent call last):
Process ForkPoolWorker-7:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-13:
Traceback (most recent call last):
Process ForkPoolWorker-14:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-16:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-17:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-18:
Traceback (most recent call last):
Process ForkPoolWorker-19:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-20:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-23:
Traceback (most recent call last):
Process ForkPoolWorker-24:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-25:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-29:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-30:
Process ForkPoolWorker-31:
Traceback (most recent call last):
Process ForkPoolWorker-32:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-33:
Process ForkPoolWorker-34:
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-35:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-36:
Process ForkPoolWorker-37:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-39:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-41:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-42:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-43:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-46:
Traceback (most recent call last):
Process ForkPoolWorker-47:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-48:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-49:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-50:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-54:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-55:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-59:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-60:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-61:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-62:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-63:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-67:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-69:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-71:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-72:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-75:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-76:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-77:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-78:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-81:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-83:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-85:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-87:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-88:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-89:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-92:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-96:
Traceback (most recent call last):
Process ForkPoolWorker-97:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-101:
Process ForkPoolWorker-102:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-103:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-105:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-108:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-114:
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-115:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-116:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-117:
Traceback (most recent call last):
Process ForkPoolWorker-118:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-121:
Traceback (most recent call last):
Process ForkPoolWorker-122:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-123:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-125:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-127:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.84s ===============================

Process ForkPoolWorker-129:
Process ForkPoolWorker-130:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-131:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-133:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-134:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-135:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-138:
Process ForkPoolWorker-139:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-140:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-141:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-143:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-146:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-147:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-148:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-149:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-151:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-155:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-156:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-158:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-160:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-163:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-164:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-166:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-168:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-169:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-170:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-173:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-176:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-177:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-178:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-179:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-180:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-182:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-184:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-185:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-190:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-194:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-195:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-197:
Process ForkPoolWorker-198:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-199:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-200:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-201:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-202:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-204:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-207:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-209:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-210:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-211:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-212:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-213:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-215:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-217:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-218:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-219:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-220:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-221:
Traceback (most recent call last):
Process ForkPoolWorker-222:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-223:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-232:
Process ForkPoolWorker-233:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-234:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-236:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-237:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-238:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-240:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-241:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-242:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-243:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-244:
Traceback (most recent call last):
Process ForkPoolWorker-245:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-246:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-248:
Process ForkPoolWorker-249:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-252:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-258:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-259:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-260:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-261:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-262:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-264:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-265:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-266:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-267:
Traceback (most recent call last):
Process ForkPoolWorker-268:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-269:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-274:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-275:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-276:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-278:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-280:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-281:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-286:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-288:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-289:
Process ForkPoolWorker-290:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-291:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-294:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-298:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-299:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-300:
Process ForkPoolWorker-301:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-303:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-304:
Process ForkPoolWorker-305:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-306:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-307:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-308:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-309:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-312:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-314:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-315:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-316:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-317:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-318:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-319:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-320:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-321:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-323:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-329:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-332:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-333:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-337:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-338:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-339:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-341:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-342:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-344:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-345:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-346:
Traceback (most recent call last):
Process ForkPoolWorker-347:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-348:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-349:
Process ForkPoolWorker-350:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-351:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-354:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-357:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-358:
Traceback (most recent call last):
Process ForkPoolWorker-359:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-360:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-361:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-362:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-363:
Traceback (most recent call last):
Process ForkPoolWorker-364:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-365:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-366:
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-369:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-370:
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-375:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-376:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-380:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-382:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-384:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-385:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-386:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-387:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-388:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-391:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-393:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-394:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-397:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-398:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-400:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-403:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-404:
Traceback (most recent call last):
Process ForkPoolWorker-405:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-406:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-409:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-411:
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-415:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-416:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-419:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-421:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-423:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-427:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-429:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-431:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-433:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-434:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-435:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-437:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-441:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-442:
Traceback (most recent call last):
Process ForkPoolWorker-443:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-445:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-447:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-449:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-452:
Process ForkPoolWorker-453:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-454:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-456:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-457:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-458:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-460:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-462:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-464:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-465:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-467:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-468:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-470:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-471:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-473:
Process ForkPoolWorker-474:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-477:
Traceback (most recent call last):
Process ForkPoolWorker-478:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-479:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-480:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-481:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-482:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-483:
Process ForkPoolWorker-484:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-487:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-488:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-491:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-497:
Process ForkPoolWorker-498:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-500:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-505:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-506:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-507:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-508:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-510:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-513:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-514:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-517:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-518:
Process ForkPoolWorker-519:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-520:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-524:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-525:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-526:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-528:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-530:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-532:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-533:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-534:
Process ForkPoolWorker-535:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-536:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-539:
Process ForkPoolWorker-540:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-541:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-542:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-543:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-547:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-548:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-550:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-551:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-553:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-554:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-557:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-558:
Traceback (most recent call last):
Process ForkPoolWorker-559:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-560:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-561:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-562:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-563:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-567:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-571:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-572:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-573:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-574:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-575:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-577:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-578:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-579:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-580:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-582:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-583:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-589:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-591:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-592:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-593:
Traceback (most recent call last):
Process ForkPoolWorker-594:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-595:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-596:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-597:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-599:
Process ForkPoolWorker-600:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-601:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-602:
Traceback (most recent call last):
Process ForkPoolWorker-603:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-605:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-606:
Traceback (most recent call last):
Process ForkPoolWorker-607:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-608:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-610:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-611:
Traceback (most recent call last):
Process ForkPoolWorker-612:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-613:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-617:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-621:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-622:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-623:
Traceback (most recent call last):
Process ForkPoolWorker-624:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-625:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-627:
"""