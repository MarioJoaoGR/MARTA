
import pytest
from typing import Callable, Iterable, List
from flutes.iterator import scanr

def add(x, y): return x + y
def mul(x, y): return x * y

# Test cases for edge cases
@pytest.mark.parametrize("func, iterable, initial, expected", [
    (add, [], 0, []),
    (mul, [], 1, []),
    (add, None, 0, TypeError),
    (mul, None, 1, TypeError),
    (add, [1, 2, 3], None, ValueError),
    (mul, [1, 2, 3], None, ValueError)
])
def test_scanr(func, iterable, initial, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            scanr(func, iterable, initial)
    else:
        assert scanr(func, iterable, initial) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py FF.. [ 66%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________ test_scanr[add-iterable0-0-expected0] _____________________

func = <function add at 0x7f185027b9c0>, iterable = [], initial = 0
expected = []

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [], 0, []),
        (mul, [], 1, []),
        (add, None, 0, TypeError),
        (mul, None, 1, TypeError),
        (add, [1, 2, 3], None, ValueError),
        (mul, [1, 2, 3], None, ValueError)
    ])
    def test_scanr(func, iterable, initial, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                scanr(func, iterable, initial)
        else:
>           assert scanr(func, iterable, initial) == expected
E           assert [0] == []
E             
E             Left contains one more item: 0
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py:23: AssertionError
____________________ test_scanr[mul-iterable1-1-expected1] _____________________

func = <function mul at 0x7f185027b560>, iterable = [], initial = 1
expected = []

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [], 0, []),
        (mul, [], 1, []),
        (add, None, 0, TypeError),
        (mul, None, 1, TypeError),
        (add, [1, 2, 3], None, ValueError),
        (mul, [1, 2, 3], None, ValueError)
    ])
    def test_scanr(func, iterable, initial, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                scanr(func, iterable, initial)
        else:
>           assert scanr(func, iterable, initial) == expected
E           assert [1] == []
E             
E             Left contains one more item: 1
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py:23: AssertionError
__________________ test_scanr[add-iterable4-None-ValueError] ___________________

func = <function add at 0x7f185027b9c0>, iterable = [1, 2, 3], initial = None
expected = <class 'ValueError'>

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [], 0, []),
        (mul, [], 1, []),
        (add, None, 0, TypeError),
        (mul, None, 1, TypeError),
        (add, [1, 2, 3], None, ValueError),
        (mul, [1, 2, 3], None, ValueError)
    ])
    def test_scanr(func, iterable, initial, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
>               scanr(func, iterable, initial)

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/iterator.py:227: in scanr
    return list(scanl(func, reversed(iterable), *args))[::-1]
flutes/flutes/iterator.py:196: in scanl
    acc = func(acc, x)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None, y = 3

>   def add(x, y): return x + y
E   TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py:6: TypeError
__________________ test_scanr[mul-iterable5-None-ValueError] ___________________

func = <function mul at 0x7f185027b560>, iterable = [1, 2, 3], initial = None
expected = <class 'ValueError'>

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [], 0, []),
        (mul, [], 1, []),
        (add, None, 0, TypeError),
        (mul, None, 1, TypeError),
        (add, [1, 2, 3], None, ValueError),
        (mul, [1, 2, 3], None, ValueError)
    ])
    def test_scanr(func, iterable, initial, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
>               scanr(func, iterable, initial)

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/iterator.py:227: in scanr
    return list(scanl(func, reversed(iterable), *args))[::-1]
flutes/flutes/iterator.py:196: in scanl
    acc = func(acc, x)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None, y = 3

>   def mul(x, y): return x * y
E   TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py::test_scanr[add-iterable0-0-expected0]
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py::test_scanr[mul-iterable1-1-expected1]
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py::test_scanr[add-iterable4-None-ValueError]
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_edge_case.py::test_scanr[mul-iterable5-None-ValueError]
========================= 4 failed, 2 passed in 0.12s ==========================

"""