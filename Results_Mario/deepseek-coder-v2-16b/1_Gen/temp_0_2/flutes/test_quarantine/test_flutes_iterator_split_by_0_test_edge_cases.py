
import pytest
from flutes.iterator import split_by

@pytest.mark.parametrize("iterable, separator, empty_segments, expected", [
    ([1, 2, 3, 4], 2, False, [[1], [3, 4]]),
    ("hello world", " ", False, ['hello', 'world']),
    ([1, 2, 3, 2, 4, 2, 5], 2, False, [[1], [], [4], [5]]),
    ("a-b-c", "-", False, ['a', 'b', 'c']),
    ([1, 2, 3, 2, 4, 2, 5], 2, True, [[1], [2], [], [4], [2], [], [5]])
])
def test_split_by(iterable, separator, empty_segments, expected):
    result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py . [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_________________ test_split_by[hello world- -False-expected1] _________________

iterable = 'hello world', separator = ' ', empty_segments = False
expected = ['hello', 'world']

    @pytest.mark.parametrize("iterable, separator, empty_segments, expected", [
        ([1, 2, 3, 4], 2, False, [[1], [3, 4]]),
        ("hello world", " ", False, ['hello', 'world']),
        ([1, 2, 3, 2, 4, 2, 5], 2, False, [[1], [], [4], [5]]),
        ("a-b-c", "-", False, ['a', 'b', 'c']),
        ([1, 2, 3, 2, 4, 2, 5], 2, True, [[1], [2], [], [4], [2], [], [5]])
    ])
    def test_split_by(iterable, separator, empty_segments, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
>       assert result == expected
E       AssertionError: assert [['h', 'e', '...r', 'l', 'd']] == ['hello', 'world']
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o'] != 'hello'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py:14: AssertionError
__________________ test_split_by[iterable2-2-False-expected2] __________________

iterable = [1, 2, 3, 2, 4, 2, ...], separator = 2, empty_segments = False
expected = [[1], [], [4], [5]]

    @pytest.mark.parametrize("iterable, separator, empty_segments, expected", [
        ([1, 2, 3, 4], 2, False, [[1], [3, 4]]),
        ("hello world", " ", False, ['hello', 'world']),
        ([1, 2, 3, 2, 4, 2, 5], 2, False, [[1], [], [4], [5]]),
        ("a-b-c", "-", False, ['a', 'b', 'c']),
        ([1, 2, 3, 2, 4, 2, 5], 2, True, [[1], [2], [], [4], [2], [], [5]])
    ])
    def test_split_by(iterable, separator, empty_segments, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
>       assert result == expected
E       assert [[1], [3], [4], [5]] == [[1], [], [4], [5]]
E         
E         At index 1 diff: [3] != []
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py:14: AssertionError
____________________ test_split_by[a-b-c---False-expected3] ____________________

iterable = 'a-b-c', separator = '-', empty_segments = False
expected = ['a', 'b', 'c']

    @pytest.mark.parametrize("iterable, separator, empty_segments, expected", [
        ([1, 2, 3, 4], 2, False, [[1], [3, 4]]),
        ("hello world", " ", False, ['hello', 'world']),
        ([1, 2, 3, 2, 4, 2, 5], 2, False, [[1], [], [4], [5]]),
        ("a-b-c", "-", False, ['a', 'b', 'c']),
        ([1, 2, 3, 2, 4, 2, 5], 2, True, [[1], [2], [], [4], [2], [], [5]])
    ])
    def test_split_by(iterable, separator, empty_segments, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
>       assert result == expected
E       AssertionError: assert [['a'], ['b'], ['c']] == ['a', 'b', 'c']
E         
E         At index 0 diff: ['a'] != 'a'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py:14: AssertionError
__________________ test_split_by[iterable4-2-True-expected4] ___________________

iterable = [1, 2, 3, 2, 4, 2, ...], separator = 2, empty_segments = True
expected = [[1], [2], [], [4], [2], [], ...]

    @pytest.mark.parametrize("iterable, separator, empty_segments, expected", [
        ([1, 2, 3, 4], 2, False, [[1], [3, 4]]),
        ("hello world", " ", False, ['hello', 'world']),
        ([1, 2, 3, 2, 4, 2, 5], 2, False, [[1], [], [4], [5]]),
        ("a-b-c", "-", False, ['a', 'b', 'c']),
        ([1, 2, 3, 2, 4, 2, 5], 2, True, [[1], [2], [], [4], [2], [], [5]])
    ])
    def test_split_by(iterable, separator, empty_segments, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, separator=separator))
>       assert result == expected
E       assert [[1], [3], [4], [5]] == [[1], [2], []... [2], [], ...]
E         
E         At index 1 diff: [3] != [2]
E         Right contains 3 more items, first extra item: [2]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py::test_split_by[hello world- -False-expected1]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py::test_split_by[iterable2-2-False-expected2]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py::test_split_by[a-b-c---False-expected3]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_cases.py::test_split_by[iterable4-2-True-expected4]
========================= 4 failed, 1 passed in 0.10s ==========================
"""