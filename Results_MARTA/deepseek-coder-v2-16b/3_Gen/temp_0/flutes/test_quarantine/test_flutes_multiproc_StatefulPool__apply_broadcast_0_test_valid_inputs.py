
import pytest
from multiprocessing import Pool, pool
from flutes.multiproc import StatefulPool
from typing import Type, Any, Tuple, Dict, Callable, Optional, Set, TypeVar
import inspect
import functools

# Assuming the following classes and types are defined elsewhere in your module
State = TypeVar('State')  # Generic type for state class
PoolType = Type[pool.Pool]  # Type hint for pool class
R = TypeVar('R')  # Generic type for result

class MyState(State):
    def initializer_function(self, arg1, arg2):
        pass

def _chain_fns(*args, **kwargs):
    fn, next_fn = kwargs.pop("fns")
    return next_fn(fn(*args, **kwargs))

def _pool_state_init(state_class, *args, **kwargs):
    state = state_class()
    if hasattr(state, 'initializer_function'):
        state.initializer_function(*args)
    return state

@pytest.fixture
def create_stateful_pool():
    def _create_stateful_pool(pool_class=Pool, state_class=MyState, state_init_args=(1, 2), args=(), kwargs={}):
        return StatefulPool(pool_class, state_class, state_init_args, args, kwargs)
    return _create_stateful_pool

@pytest.mark.parametrize("broadcast_fn", [lambda x: x * 2])
def test_valid_inputs(create_stateful_pool, broadcast_fn):
    pool = create_stateful_pool()
    result = pool._apply_broadcast(broadcast_fn, 5)
    assert result is not None
    assert result[0] == 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_valid_inputs.py _
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_valid_inputs.py:14: in <module>
    class MyState(State):
/usr/local/lib/python3.11/typing.py:1049: in __init__
    self.__constraints__ = tuple(_type_check(t, msg) for t in constraints)
/usr/local/lib/python3.11/typing.py:1049: in <genexpr>
    self.__constraints__ = tuple(_type_check(t, msg) for t in constraints)
/usr/local/lib/python3.11/typing.py:197: in _type_check
    raise TypeError(f"{msg} Got {arg!r:.100}.")
E   TypeError: TypeVar(name, constraint, ...): constraints must be types. Got (~State,).
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.22s ===============================
"""