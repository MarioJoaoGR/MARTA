
import pytest
from flutes.multiproc import StatefulPool, PoolType, State

@pytest.fixture
def create_statefulpool():
    def _create_statefulpool(pool_class=None, state_class=None, state_init_args=(), args=(), kwargs={}):
        return StatefulPool(pool_class, state_class, state_init_args, args, kwargs)
    return _create_statefulpool

def test_edge_cases(create_statefulpool):
    # Test with None inputs
    pool = create_statefulpool(None, None, (None,), (), {})
    assert isinstance(pool._pool, PoolType)
    assert pool._state_class is None
    assert pool._class_methods == set()

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

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

create_statefulpool = <function create_statefulpool.<locals>._create_statefulpool at 0x7fb5169a16c0>

    def test_edge_cases(create_statefulpool):
        # Test with None inputs
>       pool = create_statefulpool(None, None, (None,), (), {})

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:8: in _create_statefulpool
    return StatefulPool(pool_class, state_class, state_init_args, args, kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPool object at 0x7fb516998fd0>
pool_class = None, state_class = None, state_init_args = (None,), args = ()
kwargs = {'initargs': (None,), 'initializer': functools.partial(<function _pool_state_init at 0x7fb5166a4900>, None)}

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
E       TypeError: 'NoneType' object is not callable

flutes/flutes/multiproc.py:347: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.12s ===============================
"""