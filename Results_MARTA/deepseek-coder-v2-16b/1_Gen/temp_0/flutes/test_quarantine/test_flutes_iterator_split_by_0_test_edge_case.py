
import pytest
from flutes.iterator import split_by

@pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
    ([1, 2, 3, 4, 5], False, lambda x: x % 2 != 0, [[1], [3], [5]]),
    ("hello world", True, str.isupper, ["hello ", "world"]),
])
def test_edge_case(iterable, empty_segments, criterion, expected):
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
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________ test_edge_case[iterable0-False-<lambda>-expected0] ______________

iterable = [1, 2, 3, 4, 5], empty_segments = False
criterion = <function <lambda> at 0x7f0c72bd7c40>, expected = [[1], [3], [5]]

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        ([1, 2, 3, 4, 5], False, lambda x: x % 2 != 0, [[1], [3], [5]]),
        ("hello world", True, str.isupper, ["hello ", "world"]),
    ])
    def test_edge_case(iterable, empty_segments, criterion, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected
E       assert [[2], [4]] == [[1], [3], [5]]
E         
E         At index 0 diff: [2] != [1]
E         Right contains one more item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case.py:11: AssertionError
______________ test_edge_case[hello world-True-isupper-expected1] ______________

iterable = 'hello world', empty_segments = True
criterion = <method 'isupper' of 'str' objects>, expected = ['hello ', 'world']

    @pytest.mark.parametrize("iterable, empty_segments, criterion, expected", [
        ([1, 2, 3, 4, 5], False, lambda x: x % 2 != 0, [[1], [3], [5]]),
        ("hello world", True, str.isupper, ["hello ", "world"]),
    ])
    def test_edge_case(iterable, empty_segments, criterion, expected):
        result = list(split_by(iterable, empty_segments=empty_segments, criterion=criterion))
>       assert result == expected
E       AssertionError: assert [['h', 'e', '...o', ' ', ...]] == ['hello ', 'world']
E         
E         At index 0 diff: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] != 'hello '
E         Right contains one more item: 'world'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case.py::test_edge_case[iterable0-False-<lambda>-expected0]
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case.py::test_edge_case[hello world-True-isupper-expected1]
============================== 2 failed in 0.09s ===============================
"""