
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, _pool_state_init
from functools import partial
import inspect
from typing import Type, Tuple, Dict, Any, Set

class State:
    pass

@pytest.mark.parametrize("pool_class, state_class, state_init_args, args, kwargs", [
    (Pool, State, (), (1, 2), {'kwarg1': 'value1'}),
])
def test_valid_inputs(pool_class, state_class, state_init_args, args, kwargs):
    pool = StatefulPool(pool_class, state_class, state_init_args, args, kwargs)
    assert isinstance(pool._pool, pool_class)
    assert pool._state_class is state_class
    assert pool._state_init_args == state_init_args
    assert pool._args == args
    assert pool._kwargs == kwargs

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

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
_________ test_valid_inputs[Pool-State-state_init_args0-args0-kwargs0] _________

pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7fd11af78510>>
state_class = <class 'Test4DT_tests.test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.State'>
state_init_args = (), args = (1, 2)
kwargs = {'initargs': (), 'initializer': functools.partial(<function _pool_state_init at 0x7fd11abe9940>, <class 'Test4DT_tests.test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.State'>), 'kwarg1': 'value1'}

    @pytest.mark.parametrize("pool_class, state_class, state_init_args, args, kwargs", [
        (Pool, State, (), (1, 2), {'kwarg1': 'value1'}),
    ])
    def test_valid_inputs(pool_class, state_class, state_init_args, args, kwargs):
>       pool = StatefulPool(pool_class, state_class, state_init_args, args, kwargs)

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7fd11ae5c6d0>
pool_class = <bound method BaseContext.Pool of <multiprocessing.context.DefaultContext object at 0x7fd11af78510>>
state_class = <class 'Test4DT_tests.test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.State'>
state_init_args = (), args = (1, 2)
kwargs = {'initargs': (), 'initializer': functools.partial(<function _pool_state_init at 0x7fd11abe9940>, <class 'Test4DT_tests.test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.State'>), 'kwarg1': 'value1'}

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
    
>       self._pool = pool_class(*args, **kwargs)
E       TypeError: BaseContext.Pool() got an unexpected keyword argument 'kwarg1'

flutes/flutes/multiproc.py:347: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_0_test_valid_inputs.py::test_valid_inputs[Pool-State-state_init_args0-args0-kwargs0]
============================== 1 failed in 0.10s ===============================
"""