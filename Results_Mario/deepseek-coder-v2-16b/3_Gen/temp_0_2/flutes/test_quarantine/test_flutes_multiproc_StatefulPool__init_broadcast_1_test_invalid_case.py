
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, State

@pytest.fixture
def setup_statefulpool():
    class MyState(State):
        def process_item(self, item):
            return item * 2
    
    pool = StatefulPool(Pool, MyState, (1,), (), {})
    return pool

def test_invalid_case(setup_statefulpool):
    stateful_pool = setup_statefulpool
    with pytest.raises(AssertionError):
        stateful_pool._init_broadcast(_dummy=None)

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

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_invalid_case.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_invalid_case ______________________

    @pytest.fixture
    def setup_statefulpool():
>       class MyState(State):

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_invalid_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/typing.py:1049: in __init__
    self.__constraints__ = tuple(_type_check(t, msg) for t in constraints)
/usr/local/lib/python3.11/typing.py:1049: in <genexpr>
    self.__constraints__ = tuple(_type_check(t, msg) for t in constraints)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

arg = (~State,)
msg = 'TypeVar(name, constraint, ...): constraints must be types.'
is_argument = True, module = None

    def _type_check(arg, msg, is_argument=True, module=None, *, allow_special_forms=False):
        """Check that the argument is a type, and return it (internal helper).
    
        As a special case, accept None and return type(None) instead. Also wrap strings
        into ForwardRef instances. Consider several corner cases, for example plain
        special forms like Union are not valid, while Union[int, str] is OK, etc.
        The msg argument is a human-readable error message, e.g.::
    
            "Union[arg, ...]: arg should be a type."
    
        We append the repr() of the actual value (truncated to 100 chars).
        """
        invalid_generic_forms = (Generic, Protocol)
        if not allow_special_forms:
            invalid_generic_forms += (ClassVar,)
            if is_argument:
                invalid_generic_forms += (Final,)
    
        arg = _type_convert(arg, module=module, allow_special_forms=allow_special_forms)
        if (isinstance(arg, _GenericAlias) and
                arg.__origin__ in invalid_generic_forms):
            raise TypeError(f"{arg} is not valid as type argument")
        if arg in (Any, LiteralString, NoReturn, Never, Self, TypeAlias):
            return arg
        if allow_special_forms and arg in (ClassVar, Final):
            return arg
        if isinstance(arg, _SpecialForm) or arg in (Generic, Protocol):
            raise TypeError(f"Plain {arg} is not valid as type argument")
        if type(arg) is tuple:
>           raise TypeError(f"{msg} Got {arg!r:.100}.")
E           TypeError: TypeVar(name, constraint, ...): constraints must be types. Got (~State,).

/usr/local/lib/python3.11/typing.py:197: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__init_broadcast_1_test_invalid_case.py::test_invalid_case
=============================== 1 error in 0.15s ===============================
"""