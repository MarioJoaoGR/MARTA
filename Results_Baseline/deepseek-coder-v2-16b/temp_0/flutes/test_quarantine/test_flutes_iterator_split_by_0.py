
import pytest
from flutes.iterator import split_by
from typing import List, Iterable, Callable

# Helper function to create a list of integers that are even or odd based on the criterion
def is_even(n: int) -> bool: return n % 2 == 0
def is_odd(n: int) -> bool: return n % 2 != 0

# Test cases for split_by function
@pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
    # Basic usage with a list of integers
    ([1, 2, 3, 4, 5], False, is_even, [[1, 3, 5], [2, 4]]),
    
    # Including empty segments
    ([1, 2, 3, 4, 5], True, lambda x: x % 2 != 0, [[1], [], [3], [], [5], []]),
    
    # Using a string and checking for uppercase letters
    ("hello world", False, str.isupper, ["hello ", "world"]),
])
def test_split_by(iterable: Iterable[int], empty_segments: bool, criterion: Callable[[int], bool], expected: List[List[int]]):
    result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py FFF              [100%]

=================================== FAILURES ===================================
_______________ test_split_by[iterable0-False-is_even-expected0] _______________

iterable = [1, 2, 3, 4, 5], empty_segments = False
criterion = <function is_even at 0x7f6396bc0040>, expected = [[1, 3, 5], [2, 4]]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        # Basic usage with a list of integers
        ([1, 2, 3, 4, 5], False, is_even, [[1, 3, 5], [2, 4]]),
    
        # Including empty segments
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 != 0, [[1], [], [3], [], [5], []]),
    
        # Using a string and checking for uppercase letters
        ("hello world", False, str.isupper, ["hello ", "world"]),
    ])
    def test_split_by(iterable: Iterable[int], empty_segments: bool, criterion: Callable[[int], bool], expected: List[List[int]]):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected [[1, 3, 5], [2, 4]], but got [[1], [3], [5]]
E       assert [[1], [3], [5]] == [[1, 3, 5], [2, 4]]
E         
E         At index 0 diff: [1] != [1, 3, 5]
E         Left contains one more item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py:23: AssertionError
_______________ test_split_by[iterable1-True-<lambda>-expected1] _______________

iterable = [1, 2, 3, 4, 5], empty_segments = True
criterion = <function <lambda> at 0x7f6396bc0220>
expected = [[1], [], [3], [], [5], []]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        # Basic usage with a list of integers
        ([1, 2, 3, 4, 5], False, is_even, [[1, 3, 5], [2, 4]]),
    
        # Including empty segments
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 != 0, [[1], [], [3], [], [5], []]),
    
        # Using a string and checking for uppercase letters
        ("hello world", False, str.isupper, ["hello ", "world"]),
    ])
    def test_split_by(iterable: Iterable[int], empty_segments: bool, criterion: Callable[[int], bool], expected: List[List[int]]):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected [[1], [], [3], [], [5], []], but got [[], [2], [4], []]
E       assert [[], [2], [4], []] == [[1], [], [3], [], [5], []]
E         
E         At index 0 diff: [] != [1]
E         Right contains 2 more items, first extra item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py:23: AssertionError
______________ test_split_by[hello world-False-isupper-expected2] ______________

iterable = 'hello world', empty_segments = False
criterion = <method 'isupper' of 'str' objects>, expected = ['hello ', 'world']

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        # Basic usage with a list of integers
        ([1, 2, 3, 4, 5], False, is_even, [[1, 3, 5], [2, 4]]),
    
        # Including empty segments
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 != 0, [[1], [], [3], [], [5], []]),
    
        # Using a string and checking for uppercase letters
        ("hello world", False, str.isupper, ["hello ", "world"]),
    ])
    def test_split_by(iterable: Iterable[int], empty_segments: bool, criterion: Callable[[int], bool], expected: List[List[int]]):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected ['hello ', 'world'], but got [['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']]
E       assert [['h', 'e', '...o', ' ', ...]] == ['hello ', 'world']
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] != 'hello '
E         Right contains one more item: 'world'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py::test_split_by[iterable0-False-is_even-expected0]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py::test_split_by[iterable1-True-<lambda>-expected1]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py::test_split_by[hello world-False-isupper-expected2]
============================== 3 failed in 0.10s ===============================
"""