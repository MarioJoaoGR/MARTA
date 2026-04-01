
import pytest
from multiprocessing import Pool
from typing import Type, Any, Tuple, Dict, Set
import inspect
import functools

class State(object):
    pass

def _pool_state_init(state_class, *args, **kwargs):
    return state_class(*args, **kwargs)

def _chain_fns(fns, *args, **kwargs):
    for fn in fns:
        fn(*args, **kwargs)

class StatefulPool:
    _pool: 'PoolType'
    _state_class: Type[State]
    _class_methods: Set[int]
    
    def __init__(self, pool_class: Type['PoolType'], state_class: Type[State], state_init_args: Tuple[Any, ...], args: Tuple[Any, ...], kwargs: Dict[str, Any]):
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
            pool_method = getattr(self._pool, name)
            wrapped_method = self._define_method(pool_method)
            setattr(self, name, wrapped_method)

    def _define_method(self, pool_method):
        def wrapper(*args, **kwargs):
            return pool_method(*args, **kwargs)
        return wrapper

    def __getattr__(self, item):
        return getattr(self._pool, item)

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