
import pytest
from flutes.multiproc import StatefulPool
from multiprocessing import Pool
from typing import Type, Any, Tuple, Dict
from unittest.mock import MagicMock

class MyState:
    def initializer_function(self, arg1, arg2):
        pass

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Invalid pool class type
        StatefulPool(int, MyState, (), (), {})
    
    with pytest.raises(TypeError):
        # Invalid state class type
        StatefulPool(Pool, int, (), (), {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool___init___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Invalid pool class type
            StatefulPool(int, MyState, (), (), {})
    
        with pytest.raises(TypeError):
            # Invalid state class type
>           StatefulPool(Pool, int, (), (), {})

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool___init___0_test_invalid_inputs.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7f627924bb10>
pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7f627817d610>>
state_class = <class 'int'>, state_init_args = (), args = ()
kwargs = {'initargs': (), 'initializer': functools.partial(<function _pool_state_init at 0x7f62781b3920>, <class 'int'>)}

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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool___init___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.23s ===============================
"""