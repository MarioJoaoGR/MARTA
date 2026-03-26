
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

def _pool_state_init(state_class, *args, **kwargs):
    return state_class(*args, **kwargs)

def _chain_fns(fns, *args, **kwargs):
    for fn in fns:
        fn(*args, **kwargs)

@pytest.mark.parametrize("pool_class, state_class, state_init_args, args, kwargs", [
    (None, State, (1, 2), (), {}),
    (Pool, None, (1, 2), (), {}),
    (Pool, State, None, (1, 2), ()),
    (Pool, State, (1, 2), (), {'initializer': lambda: None, 'initargs': ()}),
])
def test_invalid_inputs(pool_class, state_class, state_init_args, args, kwargs):
    with pytest.raises(TypeError):
        StatefulPool(pool_class, state_class, state_init_args, args, kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py . [ 25%]
F.F                                                                      [100%]

=================================== FAILURES ===================================
________ test_invalid_inputs[Pool-None-state_init_args1-args1-kwargs1] _________

pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7f0f30421f90>>
state_class = None, state_init_args = (1, 2), args = ()
kwargs = {'initargs': (1, 2), 'initializer': functools.partial(<function _pool_state_init at 0x7f0f305351c0>, None)}

    @pytest.mark.parametrize("pool_class, state_class, state_init_args, args, kwargs", [
        (None, State, (1, 2), (), {}),
        (Pool, None, (1, 2), (), {}),
        (Pool, State, None, (1, 2), ()),
        (Pool, State, (1, 2), (), {'initializer': lambda: None, 'initargs': ()}),
    ])
    def test_invalid_inputs(pool_class, state_class, state_init_args, args, kwargs):
        with pytest.raises(TypeError):
>           StatefulPool(pool_class, state_class, state_init_args, args, kwargs)

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7f0f307281d0>
pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7f0f30421f90>>
state_class = None, state_init_args = (1, 2), args = ()
kwargs = {'initargs': (1, 2), 'initializer': functools.partial(<function _pool_state_init at 0x7f0f305351c0>, None)}

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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-3:
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-4:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-6:
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-8:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-9:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-22:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-23:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-26:
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-27:
Traceback (most recent call last):
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-29:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-32:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-35:
Traceback (most recent call last):
Process ForkPoolWorker-36:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-41:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-44:
Traceback (most recent call last):
Process ForkPoolWorker-45:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-46:
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-50:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-51:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-52:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-55:
Traceback (most recent call last):
Process ForkPoolWorker-56:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Traceback (most recent call last):
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
Process ForkPoolWorker-57:
Traceback (most recent call last):
Process ForkPoolWorker-58:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-62:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-65:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-73:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-77:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-79:
Traceback (most recent call last):
Process ForkPoolWorker-80:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-83:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-84:
Traceback (most recent call last):
Process ForkPoolWorker-85:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-88:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-93:
Traceback (most recent call last):
Process ForkPoolWorker-94:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-97:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-98:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-103:
Traceback (most recent call last):
Process ForkPoolWorker-104:
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-113:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-114:
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-118:
Process ForkPoolWorker-119:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Traceback (most recent call last):
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
Process ForkPoolWorker-120:
Traceback (most recent call last):
Process ForkPoolWorker-121:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
________ test_invalid_inputs[Pool-State-state_init_args3-args3-kwargs3] ________

pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7f0f30421f90>>
state_class = ~State, state_init_args = (1, 2), args = ()
kwargs = {'initargs': [((1, 2), {}), ((), {})], 'initializer': functools.partial(<function _chain_fns at 0x7f0f3055f920>, fns=[functools.partial(<function _pool_state_init at 0x7f0f305351c0>, ~State), <function <lambda> at 0x7f0f304372e0>])}

    @pytest.mark.parametrize("pool_class, state_class, state_init_args, args, kwargs", [
        (None, State, (1, 2), (), {}),
        (Pool, None, (1, 2), (), {}),
        (Pool, State, None, (1, 2), ()),
        (Pool, State, (1, 2), (), {'initializer': lambda: None, 'initargs': ()}),
    ])
    def test_invalid_inputs(pool_class, state_class, state_init_args, args, kwargs):
        with pytest.raises(TypeError):
>           StatefulPool(pool_class, state_class, state_init_args, args, kwargs)

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7f0f2eb49350>
pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7f0f30421f90>>
state_class = ~State, state_init_args = (1, 2), args = ()
kwargs = {'initargs': [((1, 2), {}), ((), {})], 'initializer': functools.partial(<function _chain_fns at 0x7f0f3055f920>, fns=[functools.partial(<function _pool_state_init at 0x7f0f305351c0>, ~State), <function <lambda> at 0x7f0f304372e0>])}

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
Process ForkPoolWorker-473:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-474:
Traceback (most recent call last):
Process ForkPoolWorker-475:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-476:
Traceback (most recent call last):
Process ForkPoolWorker-477:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-479:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-480:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-482:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-483:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-484:
Traceback (most recent call last):
Process ForkPoolWorker-485:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-488:
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-491:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-492:
Traceback (most recent call last):
Process ForkPoolWorker-493:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-495:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-500:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-501:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-503:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-505:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-506:
Process ForkPoolWorker-507:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-510:
Traceback (most recent call last):
Process ForkPoolWorker-511:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-513:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-516:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-518:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-524:
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
Process ForkPoolWorker-527:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-528:
Traceback (most recent call last):
Process ForkPoolWorker-529:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-530:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-531:
Traceback (most recent call last):
Process ForkPoolWorker-532:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-534:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-535:
Process ForkPoolWorker-536:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-538:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-537:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-539:
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
Process ForkPoolWorker-540:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-542:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-543:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-544:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-547:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-548:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-551:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-553:
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
Process ForkPoolWorker-554:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-558:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-559:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-562:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-564:
Traceback (most recent call last):
Process ForkPoolWorker-565:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-568:
Traceback (most recent call last):
Process ForkPoolWorker-567:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-570:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-569:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-573:
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
Process ForkPoolWorker-576:
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-575:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-577:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-579:
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-583:
Traceback (most recent call last):
Process ForkPoolWorker-584:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-587:
Traceback (most recent call last):
Process ForkPoolWorker-589:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-591:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-590:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-593:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-596:
Traceback (most recent call last):
Process ForkPoolWorker-597:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-598:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-600:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-601:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-604:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-603:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-607:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-610:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-609:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-611:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-613:
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
Traceback (most recent call last):
Process ForkPoolWorker-615:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-616:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-617:
Traceback (most recent call last):
Process ForkPoolWorker-618:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-619:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-620:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-622:
Traceback (most recent call last):
Process ForkPoolWorker-621:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
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
Process ForkPoolWorker-625:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-626:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-627:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-628:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-629:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-630:
Process ForkPoolWorker-631:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-632:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-633:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-635:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-634:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-637:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-636:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-638:
Traceback (most recent call last):
Process ForkPoolWorker-639:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-640:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-641:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-642:
Traceback (most recent call last):
Process ForkPoolWorker-643:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-644:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-645:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-646:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-648:
Process ForkPoolWorker-647:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-649:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-650:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-651:
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-652:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-653:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-654:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-655:
Process ForkPoolWorker-656:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-657:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-658:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-659:
Process ForkPoolWorker-660:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-662:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-661:
Traceback (most recent call last):
Process ForkPoolWorker-663:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-664:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-665:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-666:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-667:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-668:
Process ForkPoolWorker-669:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-670:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-671:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-672:
Traceback (most recent call last):
Process ForkPoolWorker-673:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-675:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-674:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-676:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-677:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-678:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-679:
Traceback (most recent call last):
Process ForkPoolWorker-680:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-681:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-682:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-683:
Process ForkPoolWorker-684:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-685:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-686:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-687:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-689:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-688:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-690:
Process ForkPoolWorker-691:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-692:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-693:
Traceback (most recent call last):
Process ForkPoolWorker-694:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-695:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-696:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-697:
Traceback (most recent call last):
Process ForkPoolWorker-698:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-699:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-700:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-701:
Traceback (most recent call last):
Process ForkPoolWorker-702:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-703:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-704:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-705:
Traceback (most recent call last):
Process ForkPoolWorker-706:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-707:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-708:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-709:
Traceback (most recent call last):
Process ForkPoolWorker-711:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-710:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-712:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-713:
Traceback (most recent call last):
Process ForkPoolWorker-714:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-715:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-716:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-717:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-719:
Traceback (most recent call last):
Process ForkPoolWorker-718:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-720:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-721:
Traceback (most recent call last):
Process ForkPoolWorker-722:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-723:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-725:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-724:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py::test_invalid_inputs[Pool-None-state_init_args1-args1-kwargs1]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__define_method_0_test_invalid_inputs.py::test_invalid_inputs[Pool-State-state_init_args3-args3-kwargs3]
========================= 2 failed, 2 passed in 1.08s ==========================

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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-136:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-137:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-138:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-139:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-140:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
Process ForkPoolWorker-142:
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
Process ForkPoolWorker-146:
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
TypeError: 'NoneType' object is not callable
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-150:
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-152:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-153:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-157:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-158:
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
Traceback (most recent call last):
Process ForkPoolWorker-162:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-165:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-169:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-172:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-173:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-174:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-175:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-177:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-181:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-191:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-193:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-195:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-197:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-202:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-203:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-206:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-212:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-214:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-218:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-220:
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-224:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-226:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-227:
Traceback (most recent call last):
Process ForkPoolWorker-228:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-230:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-239:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-244:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-246:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-247:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-253:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-254:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-258:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-259:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-260:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-261:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-269:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-271:
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
Traceback (most recent call last):
Process ForkPoolWorker-274:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-278:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-283:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-286:
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
Process ForkPoolWorker-287:
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-291:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-293:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-295:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-296:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-297:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-301:
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
Process ForkPoolWorker-302:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-304:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
Process ForkPoolWorker-306:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-310:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-312:
Process ForkPoolWorker-313:
Process ForkPoolWorker-314:
Process ForkPoolWorker-315:
Process ForkPoolWorker-316:
Process ForkPoolWorker-317:
Process ForkPoolWorker-318:
Process ForkPoolWorker-319:
Process ForkPoolWorker-320:
Process ForkPoolWorker-321:
Process ForkPoolWorker-322:
Process ForkPoolWorker-323:
Process ForkPoolWorker-324:
Process ForkPoolWorker-325:
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
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
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
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-328:
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
Process ForkPoolWorker-329:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-330:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
TypeError: 'NoneType' object is not callable
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-332:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-334:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-335:
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
Process ForkPoolWorker-343:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-349:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
Process ForkPoolWorker-351:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-353:
Process ForkPoolWorker-354:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-356:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-363:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-365:
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-370:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
Process ForkPoolWorker-372:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-373:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-375:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-376:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-377:
Process ForkPoolWorker-378:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-385:
Process ForkPoolWorker-386:
Process ForkPoolWorker-387:
Process ForkPoolWorker-388:
Process ForkPoolWorker-389:
Process ForkPoolWorker-390:
Process ForkPoolWorker-391:
Process ForkPoolWorker-392:
Process ForkPoolWorker-393:
Process ForkPoolWorker-394:
Process ForkPoolWorker-395:
Process ForkPoolWorker-396:
Process ForkPoolWorker-397:
Process ForkPoolWorker-398:
Process ForkPoolWorker-399:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-401:
Traceback (most recent call last):
Traceback (most recent call last):
Process ForkPoolWorker-402:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: 'NoneType' object is not callable
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
TypeError: 'NoneType' object is not callable
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: 'NoneType' object is not callable
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-404:
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
Traceback (most recent call last):
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-409:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-413:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-415:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-416:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
Process ForkPoolWorker-425:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-436:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-452:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-455:
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-459:
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
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-461:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
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
Process ForkPoolWorker-469:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-726:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-727:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-728:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-730:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-729:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-731:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-732:
Traceback (most recent call last):
Process ForkPoolWorker-733:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-735:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-734:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-737:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-736:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-738:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-739:
Traceback (most recent call last):
Process ForkPoolWorker-740:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-741:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-742:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-743:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-744:
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-745:
Traceback (most recent call last):
Process ForkPoolWorker-746:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-747:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-748:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-749:
Traceback (most recent call last):
Process ForkPoolWorker-750:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-751:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-752:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-753:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-754:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-755:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-756:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-757:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-758:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-759:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-760:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-762:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-761:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-763:
Process ForkPoolWorker-764:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-765:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-766:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-767:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-768:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-769:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
Process ForkPoolWorker-770:
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-772:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-771:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-773:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-774:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-775:
Process ForkPoolWorker-776:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-777:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Process ForkPoolWorker-778:
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-779:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-780:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-781:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-782:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-783:
Process ForkPoolWorker-785:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-784:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-787:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-786:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-788:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-789:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-790:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-791:
Traceback (most recent call last):
Process ForkPoolWorker-792:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-793:
Process ForkPoolWorker-794:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-795:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-797:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-796:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-798:
Process ForkPoolWorker-799:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-800:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-801:
Traceback (most recent call last):
Process ForkPoolWorker-802:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-803:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-804:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-805:
Process ForkPoolWorker-806:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-807:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-808:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-809:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-810:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-811:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-812:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-813:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-814:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
Process ForkPoolWorker-815:
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-817:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-816:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-818:
Traceback (most recent call last):
Process ForkPoolWorker-819:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-820:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-821:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-822:
Traceback (most recent call last):
Process ForkPoolWorker-823:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-824:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-825:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-827:
Traceback (most recent call last):
Process ForkPoolWorker-826:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-829:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-828:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-830:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-831:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-832:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-834:
Process ForkPoolWorker-833:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-835:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-836:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-838:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-837:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-839:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-840:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-841:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-842:
Process ForkPoolWorker-843:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-844:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-845:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-846:
Process ForkPoolWorker-847:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-848:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-849:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-851:
Process ForkPoolWorker-850:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-852:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-853:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-855:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-854:
Process ForkPoolWorker-857:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-856:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-858:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-859:
Traceback (most recent call last):
Process ForkPoolWorker-860:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-861:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-863:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-862:
Traceback (most recent call last):
Process ForkPoolWorker-864:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-865:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-867:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-866:
Process ForkPoolWorker-869:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-868:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-870:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-871:
Process ForkPoolWorker-872:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-873:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-874:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-875:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-876:
Traceback (most recent call last):
Process ForkPoolWorker-878:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-877:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-879:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-880:
Traceback (most recent call last):
Process ForkPoolWorker-881:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-882:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-883:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-885:
Traceback (most recent call last):
Process ForkPoolWorker-884:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-886:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-887:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-888:
Traceback (most recent call last):
Process ForkPoolWorker-889:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-891:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-890:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-892:
Traceback (most recent call last):
Process ForkPoolWorker-893:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-894:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-895:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-896:
Traceback (most recent call last):
Process ForkPoolWorker-897:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-898:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-899:
Traceback (most recent call last):
Process ForkPoolWorker-901:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-900:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-903:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-902:
Process ForkPoolWorker-904:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-905:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-906:
Traceback (most recent call last):
Process ForkPoolWorker-907:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-908:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-909:
Traceback (most recent call last):
Process ForkPoolWorker-910:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-911:
Process ForkPoolWorker-912:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-913:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-914:
Traceback (most recent call last):
Process ForkPoolWorker-915:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-916:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-918:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-917:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-919:
Process ForkPoolWorker-920:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-921:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-922:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-923:
Process ForkPoolWorker-924:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-925:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-926:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-927:
Process ForkPoolWorker-928:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-929:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-930:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-931:
Process ForkPoolWorker-932:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-933:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-934:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-935:
Process ForkPoolWorker-936:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
Process ForkPoolWorker-937:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-938:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-939:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-940:
Process ForkPoolWorker-941:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-942:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-943:
Traceback (most recent call last):
Process ForkPoolWorker-944:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-945:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-947:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-946:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-949:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-948:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-951:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-950:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-953:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-952:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-955:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-954:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-956:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-957:
Process ForkPoolWorker-958:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-959:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-960:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-961:
Traceback (most recent call last):
Process ForkPoolWorker-962:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-964:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-963:
Traceback (most recent call last):
Process ForkPoolWorker-966:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-965:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-967:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-968:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-969:
Traceback (most recent call last):
Process ForkPoolWorker-970:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
TypeError: _chain_fns() got multiple values for argument 'fns'
Process ForkPoolWorker-971:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-972:
Traceback (most recent call last):
Process ForkPoolWorker-973:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
TypeError: _chain_fns() got multiple values for argument 'fns'
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-975:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-976:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-977:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-978:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-979:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-980:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-981:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-982:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-983:
Traceback (most recent call last):
Process ForkPoolWorker-984:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-985:
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Traceback (most recent call last):
Process ForkPoolWorker-986:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-987:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-988:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-989:
Traceback (most recent call last):
Process ForkPoolWorker-990:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-991:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-992:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-993:
Traceback (most recent call last):
Process ForkPoolWorker-994:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-995:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-996:
Process ForkPoolWorker-997:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-998:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-999:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-1000:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-1001:
Traceback (most recent call last):
Process ForkPoolWorker-1002:
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-1003:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
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
Process ForkPoolWorker-1004:
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 109, in worker
    initializer(*initargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 184, in _pool_state_init
    state_obj = state_class(*args, **kwargs)  # type: ignore[call-arg]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable
Process ForkPoolWorker-1005:
Exception ignored in: <function Pool.__del__ at 0x7f0f3055c900>
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