
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

# Mocking the get_worker_id function since it's not defined in this context
def mock_get_worker_id():
    return 12345

@pytest.fixture(autouse=True)
def setup_mocks():
    # Setup a mock for get_worker_id
    StatefulPool._get_worker_id = lambda self: mock_get_worker_id()

class MyState(State):
    def process_item(self, item):
        return item * 2

def test_statefulpool_init():
    pool_class = Pool
    state_class = MyState
    state_init_args = (1,)
    args = ()
    kwargs = {}

    # Initialize the StatefulPool instance
    stateful_pool = StatefulPool(pool_class, state_class, state_init_args, args, kwargs)

    # Assertions to verify the initialization
    assert isinstance(stateful_pool._pool, pool_class)
    assert stateful_pool._state_class == state_class
    assert stateful_pool._class_methods == {id(MyState.process_item)}

def test_statefulpool_init_with_initializer():
    pool_class = Pool
    state_class = MyState
    state_init_args = (1,)
    args = ()
    kwargs = {"initializer": lambda: None, "initargs": ()}

    # Initialize the StatefulPool instance with initializer
    stateful_pool = StatefulPool(pool_class, state_class, state_init_args, args, kwargs)

    # Assertions to verify the initialization with initializer
    assert isinstance(stateful_pool._pool, pool_class)
    assert stateful_pool._state_class == state_class
    assert stateful_pool._class_methods == {id(MyState.process_item)}

def test_statefulpool_init_with_invalid_initializer():
    pool_class = Pool
    state_class = MyState
    state_init_args = (1,)
    args = ()
    kwargs = {"initializer": "not a callable", "initargs": ()}

    # Initialize the StatefulPool instance with an invalid initializer
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
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_edge_cases.py _
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_edge_cases.py:15: in <module>
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
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.22s ===============================
"""