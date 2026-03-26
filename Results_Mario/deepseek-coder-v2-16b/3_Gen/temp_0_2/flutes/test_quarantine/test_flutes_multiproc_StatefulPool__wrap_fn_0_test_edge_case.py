
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, _pool_fn_with_state, _chain_fns
from typing import Type, Any, Tuple, Dict, Callable, Set, TypeVar, Generic, Optional
import inspect
import functools

T = TypeVar('T')
R = TypeVar('R')
State = TypeVar('State')
PoolType = TypeVar('PoolType', bound='Pool')

class MyState(State):
    def process_item(self, item: T) -> R:
        return item * 2

def test_edge_case():
    pool = StatefulPool(Pool, MyState, (10,), (), {})
    results = pool.map(lambda x: x + 1, [1, 2, 3])
    assert results == [2, 4, 6]

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
_ ERROR collecting Test4DT_tests/test_flutes_multiproc_StatefulPool__wrap_fn_0_test_edge_case.py _
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__wrap_fn_0_test_edge_case.py:14: in <module>
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
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__wrap_fn_0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""