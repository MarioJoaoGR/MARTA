
import pytest
from flutes.iterator import split_by

@pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
    ([1, 2, 3, 4], False, 3, [[1, 2], [3, 4]]),
    ([1, 2, 3, 4], True, 3, [[1, 2], [], [3, 4]]),
    ("Hello world", False, " ", ["Hello", "world"]),
    ("banana", False, "a", ["b", "n", "n"]),
    ([5, 6, 7, 8, 9], True, 7, [[5, 6], [], [7, 8], [9]])
])
def test_valid_input_string(iterable, empty_segments, separator, expected):
    result = list(split_by(iterable, empty_segments, separator=separator))
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

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_____________ test_valid_input_string[iterable0-False-3-expected0] _____________

iterable = [1, 2, 3, 4], empty_segments = False, separator = 3
expected = [[1, 2], [3, 4]]

    @pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
        ([1, 2, 3, 4], False, 3, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4], True, 3, [[1, 2], [], [3, 4]]),
        ("Hello world", False, " ", ["Hello", "world"]),
        ("banana", False, "a", ["b", "n", "n"]),
        ([5, 6, 7, 8, 9], True, 7, [[5, 6], [], [7, 8], [9]])
    ])
    def test_valid_input_string(iterable, empty_segments, separator, expected):
        result = list(split_by(iterable, empty_segments, separator=separator))
>       assert result == expected
E       assert [[1, 2], [4]] == [[1, 2], [3, 4]]
E         
E         At index 1 diff: [4] != [3, 4]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py:14: AssertionError
_____________ test_valid_input_string[iterable1-True-3-expected1] ______________

iterable = [1, 2, 3, 4], empty_segments = True, separator = 3
expected = [[1, 2], [], [3, 4]]

    @pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
        ([1, 2, 3, 4], False, 3, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4], True, 3, [[1, 2], [], [3, 4]]),
        ("Hello world", False, " ", ["Hello", "world"]),
        ("banana", False, "a", ["b", "n", "n"]),
        ([5, 6, 7, 8, 9], True, 7, [[5, 6], [], [7, 8], [9]])
    ])
    def test_valid_input_string(iterable, empty_segments, separator, expected):
        result = list(split_by(iterable, empty_segments, separator=separator))
>       assert result == expected
E       assert [[1, 2], [4]] == [[1, 2], [], [3, 4]]
E         
E         At index 1 diff: [4] != []
E         Right contains one more item: [3, 4]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py:14: AssertionError
____________ test_valid_input_string[Hello world-False- -expected2] ____________

iterable = 'Hello world', empty_segments = False, separator = ' '
expected = ['Hello', 'world']

    @pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
        ([1, 2, 3, 4], False, 3, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4], True, 3, [[1, 2], [], [3, 4]]),
        ("Hello world", False, " ", ["Hello", "world"]),
        ("banana", False, "a", ["b", "n", "n"]),
        ([5, 6, 7, 8, 9], True, 7, [[5, 6], [], [7, 8], [9]])
    ])
    def test_valid_input_string(iterable, empty_segments, separator, expected):
        result = list(split_by(iterable, empty_segments, separator=separator))
>       assert result == expected
E       AssertionError: assert [['H', 'e', '...r', 'l', 'd']] == ['Hello', 'world']
E         
E         At index 0 diff: ['H', 'e', 'l', 'l', 'o'] != 'Hello'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py:14: AssertionError
______________ test_valid_input_string[banana-False-a-expected3] _______________

iterable = 'banana', empty_segments = False, separator = 'a'
expected = ['b', 'n', 'n']

    @pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
        ([1, 2, 3, 4], False, 3, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4], True, 3, [[1, 2], [], [3, 4]]),
        ("Hello world", False, " ", ["Hello", "world"]),
        ("banana", False, "a", ["b", "n", "n"]),
        ([5, 6, 7, 8, 9], True, 7, [[5, 6], [], [7, 8], [9]])
    ])
    def test_valid_input_string(iterable, empty_segments, separator, expected):
        result = list(split_by(iterable, empty_segments, separator=separator))
>       assert result == expected
E       AssertionError: assert [['b'], ['n'], ['n']] == ['b', 'n', 'n']
E         
E         At index 0 diff: ['b'] != 'b'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py:14: AssertionError
_____________ test_valid_input_string[iterable4-True-7-expected4] ______________

iterable = [5, 6, 7, 8, 9], empty_segments = True, separator = 7
expected = [[5, 6], [], [7, 8], [9]]

    @pytest.mark.parametrize("iterable, empty_segments, separator, expected", [
        ([1, 2, 3, 4], False, 3, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4], True, 3, [[1, 2], [], [3, 4]]),
        ("Hello world", False, " ", ["Hello", "world"]),
        ("banana", False, "a", ["b", "n", "n"]),
        ([5, 6, 7, 8, 9], True, 7, [[5, 6], [], [7, 8], [9]])
    ])
    def test_valid_input_string(iterable, empty_segments, separator, expected):
        result = list(split_by(iterable, empty_segments, separator=separator))
>       assert result == expected
E       assert [[5, 6], [8, 9]] == [[5, 6], [], [7, 8], [9]]
E         
E         At index 1 diff: [8, 9] != []
E         Right contains 2 more items, first extra item: [7, 8]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py::test_valid_input_string[iterable0-False-3-expected0]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py::test_valid_input_string[iterable1-True-3-expected1]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py::test_valid_input_string[Hello world-False- -expected2]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py::test_valid_input_string[banana-False-a-expected3]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_string.py::test_valid_input_string[iterable4-True-7-expected4]
============================== 5 failed in 0.10s ===============================
"""