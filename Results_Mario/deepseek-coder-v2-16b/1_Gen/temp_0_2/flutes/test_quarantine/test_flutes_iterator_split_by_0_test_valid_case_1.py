
import pytest
from flutes.iterator import split_by

@pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
    ([1, 2, 3, 4, 5], False, lambda x: x % 2 == 0, [[1, 2], [3, 4], [5]]),
    ([1, 2, 3, 4, 5], True, lambda x: x % 2 == 0, [[1], [2], [3], [4], [5]]),
    ("hello world", False, str.isspace, ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']),
    ([1, 2, None, 3, None, 4, 5], False, lambda x: x is None, [[1, 2], [None, 3], [None, 4], [5]])
])
def test_valid_case_1(iterable, empty_segments, criterion, expected):
    result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
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
collected 4 items

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
____________ test_valid_case_1[iterable0-False-<lambda>-expected0] _____________

iterable = [1, 2, 3, 4, 5], empty_segments = False
criterion = <function <lambda> at 0x7f70de1e1260>
expected = [[1, 2], [3, 4], [5]]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        ([1, 2, 3, 4, 5], False, lambda x: x % 2 == 0, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 == 0, [[1], [2], [3], [4], [5]]),
        ("hello world", False, str.isspace, ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']),
        ([1, 2, None, 3, None, 4, 5], False, lambda x: x is None, [[1, 2], [None, 3], [None, 4], [5]])
    ])
    def test_valid_case_1(iterable, empty_segments, criterion, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected
E       assert [[1], [3], [5]] == [[1, 2], [3, 4], [5]]
E         
E         At index 0 diff: [1] != [1, 2]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py:13: AssertionError
_____________ test_valid_case_1[iterable1-True-<lambda>-expected1] _____________

iterable = [1, 2, 3, 4, 5], empty_segments = True
criterion = <function <lambda> at 0x7f70de1e07c0>
expected = [[1], [2], [3], [4], [5]]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        ([1, 2, 3, 4, 5], False, lambda x: x % 2 == 0, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 == 0, [[1], [2], [3], [4], [5]]),
        ("hello world", False, str.isspace, ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']),
        ([1, 2, None, 3, None, 4, 5], False, lambda x: x is None, [[1, 2], [None, 3], [None, 4], [5]])
    ])
    def test_valid_case_1(iterable, empty_segments, criterion, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected
E       assert [[1], [3], [5]] == [[1], [2], [3], [4], [5]]
E         
E         At index 1 diff: [3] != [2]
E         Right contains 2 more items, first extra item: [4]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py:13: AssertionError
____________ test_valid_case_1[hello world-False-isspace-expected2] ____________

iterable = 'hello world', empty_segments = False
criterion = <method 'isspace' of 'str' objects>
expected = ['h', 'e', 'l', 'l', 'o', ' ', ...]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        ([1, 2, 3, 4, 5], False, lambda x: x % 2 == 0, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 == 0, [[1], [2], [3], [4], [5]]),
        ("hello world", False, str.isspace, ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']),
        ([1, 2, None, 3, None, 4, 5], False, lambda x: x is None, [[1, 2], [None, 3], [None, 4], [5]])
    ])
    def test_valid_case_1(iterable, empty_segments, criterion, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected
E       AssertionError: assert [['h', 'e', '...r', 'l', 'd']] == ['h', 'e', 'l...'o', ' ', ...]
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o'] != 'h'
E         Right contains 9 more items, first extra item: 'l'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py:13: AssertionError
____________ test_valid_case_1[iterable3-False-<lambda>-expected3] _____________

iterable = [1, 2, None, 3, None, 4, ...], empty_segments = False
criterion = <function <lambda> at 0x7f70de1e0a40>
expected = [[1, 2], [None, 3], [None, 4], [5]]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        ([1, 2, 3, 4, 5], False, lambda x: x % 2 == 0, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4, 5], True, lambda x: x % 2 == 0, [[1], [2], [3], [4], [5]]),
        ("hello world", False, str.isspace, ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']),
        ([1, 2, None, 3, None, 4, 5], False, lambda x: x is None, [[1, 2], [None, 3], [None, 4], [5]])
    ])
    def test_valid_case_1(iterable, empty_segments, criterion, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected
E       assert [[1, 2], [3], [4, 5]] == [[1, 2], [Non...None, 4], [5]]
E         
E         At index 1 diff: [3] != [None, 3]
E         Right contains one more item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py::test_valid_case_1[iterable0-False-<lambda>-expected0]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py::test_valid_case_1[iterable1-True-<lambda>-expected1]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py::test_valid_case_1[hello world-False-isspace-expected2]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_case_1.py::test_valid_case_1[iterable3-False-<lambda>-expected3]
============================== 4 failed in 0.09s ===============================
"""