
import pytest
from multiprocessing import Pool
from typing import Type, Any, Tuple, Dict
from flutes.multiproc import StatefulPool, State
import inspect
import functools

class MyState(State):
    def process_item(self, item):
        return item * 2

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Invalid pool class type
        StatefulPool(int, MyState, (1,), (), {})
        
    with pytest.raises(TypeError):
        # Invalid state class type
        StatefulPool(Pool, int, (1,), (), {})
        
    with pytest.raises(TypeError):
        # Invalid state initialization arguments type
        StatefulPool(Pool, MyState, "invalid", (), {})
        
    with pytest.raises(TypeError):
        # Invalid positional arguments type
        StatefulPool(Pool, MyState, (1,), "invalid", {})
        
    with pytest.raises(TypeError):
        # Invalid keyword arguments type
        StatefulPool(Pool, MyState, (1,), (), "invalid")

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
_ ERROR collecting Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_invalid_inputs.py _
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_invalid_inputs.py:9: in <module>
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
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.21s ===============================
"""