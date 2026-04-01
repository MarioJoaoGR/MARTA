
import pytest
from flutes.multiproc import FuncWrapper

def example_function(a, b=None):
    return a + (b or 0)

@pytest.mark.parametrize("args, kwds, expected", [
    ((1,), {'b': None}, 1),
    ((1,), {}, 1),
    ((1,), {'b': 2}, 3),
    ((), {}, 0),
    (None, {}, TypeError),
    ((1,), None, TypeError),
    ((), {'b': None}, 0),
])
def test_edge_cases(args, kwds, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
            wrapper()
    else:
        wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
        assert wrapper(*args, **kwds) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py F [ 14%]
FFF..F                                                                   [100%]

=================================== FAILURES ===================================
________________________ test_edge_cases[args0-kwds0-1] ________________________

args = (1,), kwds = {'b': None}, expected = 1

    @pytest.mark.parametrize("args, kwds, expected", [
        ((1,), {'b': None}, 1),
        ((1,), {}, 1),
        ((1,), {'b': 2}, 3),
        ((), {}, 0),
        (None, {}, TypeError),
        ((1,), None, TypeError),
        ((), {'b': None}, 0),
    ])
    def test_edge_cases(args, kwds, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
                wrapper()
        else:
            wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
>           assert wrapper(*args, **kwds) == expected
E           TypeError: FuncWrapper.__call__() got an unexpected keyword argument 'b'

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py:24: TypeError
________________________ test_edge_cases[args1-kwds1-1] ________________________

args = (1,), kwds = {}, expected = 1

    @pytest.mark.parametrize("args, kwds, expected", [
        ((1,), {'b': None}, 1),
        ((1,), {}, 1),
        ((1,), {'b': 2}, 3),
        ((), {}, 0),
        (None, {}, TypeError),
        ((1,), None, TypeError),
        ((), {'b': None}, 0),
    ])
    def test_edge_cases(args, kwds, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
                wrapper()
        else:
            wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
>           assert wrapper(*args, **kwds) == expected
E           assert 2 == 1
E            +  where 2 = <flutes.multiproc.FuncWrapper object at 0x7f920b07bad0>(*(1,), **{})

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py:24: AssertionError
________________________ test_edge_cases[args2-kwds2-3] ________________________

args = (1,), kwds = {'b': 2}, expected = 3

    @pytest.mark.parametrize("args, kwds, expected", [
        ((1,), {'b': None}, 1),
        ((1,), {}, 1),
        ((1,), {'b': 2}, 3),
        ((), {}, 0),
        (None, {}, TypeError),
        ((1,), None, TypeError),
        ((), {'b': None}, 0),
    ])
    def test_edge_cases(args, kwds, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
                wrapper()
        else:
            wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
>           assert wrapper(*args, **kwds) == expected
E           TypeError: FuncWrapper.__call__() got an unexpected keyword argument 'b'

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py:24: TypeError
________________________ test_edge_cases[args3-kwds3-0] ________________________

args = (), kwds = {}, expected = 0

    @pytest.mark.parametrize("args, kwds, expected", [
        ((1,), {'b': None}, 1),
        ((1,), {}, 1),
        ((1,), {'b': 2}, 3),
        ((), {}, 0),
        (None, {}, TypeError),
        ((1,), None, TypeError),
        ((), {'b': None}, 0),
    ])
    def test_edge_cases(args, kwds, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
                wrapper()
        else:
            wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
>           assert wrapper(*args, **kwds) == expected

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.FuncWrapper object at 0x7f920b099b10>, args = ()

    def __call__(self, *args):
>       return self.fn(*args, *self.args, **self.kwds)
E       TypeError: example_function() missing 1 required positional argument: 'a'

flutes/flutes/multiproc.py:219: TypeError
________________________ test_edge_cases[args6-kwds6-0] ________________________

args = (), kwds = {'b': None}, expected = 0

    @pytest.mark.parametrize("args, kwds, expected", [
        ((1,), {'b': None}, 1),
        ((1,), {}, 1),
        ((1,), {'b': 2}, 3),
        ((), {}, 0),
        (None, {}, TypeError),
        ((1,), None, TypeError),
        ((), {'b': None}, 0),
    ])
    def test_edge_cases(args, kwds, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
                wrapper()
        else:
            wrapper = FuncWrapper(example_function, args=args, kwds=kwds)
>           assert wrapper(*args, **kwds) == expected
E           TypeError: FuncWrapper.__call__() got an unexpected keyword argument 'b'

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py:24: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py::test_edge_cases[args0-kwds0-1]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py::test_edge_cases[args1-kwds1-1]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py::test_edge_cases[args2-kwds2-3]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py::test_edge_cases[args3-kwds3-0]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___1_test_edge_cases.py::test_edge_cases[args6-kwds6-0]
========================= 5 failed, 2 passed in 0.10s ==========================

"""