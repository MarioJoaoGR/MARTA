
import pytest
from flutes.iterator import split_by
from typing import List, Iterable, Callable

def is_even(n: int) -> bool: return n % 2 == 0

# Test cases for the function `split_by`
def test_split_by_default():
    iterable = [1, 2, 3, 4, 5]
    result = list(split_by(iterable, criterion=is_even))
    assert result == [[1, 3, 5], [2, 4]]

def test_split_by_with_empty_segments():
    iterable = [1, 2, 3, 4, 5]
    result = list(split_by(iterable, empty_segments=True, criterion=is_even))
    assert result == [[1], [], [3], [], [5], []]

def test_split_by_string():
    iterable = "hello world"
    result = list(split_by(iterable, criterion=str.isupper))
    assert result == ["hello ", "world"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_split_by_default _____________________________

    def test_split_by_default():
        iterable = [1, 2, 3, 4, 5]
        result = list(split_by(iterable, criterion=is_even))
>       assert result == [[1, 3, 5], [2, 4]]
E       assert [[1], [3], [5]] == [[1, 3, 5], [2, 4]]
E         
E         At index 0 diff: [1] != [1, 3, 5]
E         Left contains one more item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py:12: AssertionError
______________________ test_split_by_with_empty_segments _______________________

    def test_split_by_with_empty_segments():
        iterable = [1, 2, 3, 4, 5]
        result = list(split_by(iterable, empty_segments=True, criterion=is_even))
>       assert result == [[1], [], [3], [], [5], []]
E       assert [[1], [3], [5]] == [[1], [], [3], [], [5], []]
E         
E         At index 1 diff: [3] != []
E         Right contains 3 more items, first extra item: []
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py:17: AssertionError
_____________________________ test_split_by_string _____________________________

    def test_split_by_string():
        iterable = "hello world"
        result = list(split_by(iterable, criterion=str.isupper))
>       assert result == ["hello ", "world"]
E       AssertionError: assert [['h', 'e', '...o', ' ', ...]] == ['hello ', 'world']
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] != 'hello '
E         Right contains one more item: 'world'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py::test_split_by_default
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py::test_split_by_with_empty_segments
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_happy_path.py::test_split_by_string
============================== 3 failed in 0.10s ===============================

"""