
import pytest
from isort.sorting import naturally, _natural_keys
from typing import Iterable, Callable, Any

@pytest.mark.parametrize("to_sort, key, reverse, expected", [
    (['item12', 'item2', 'item1'], None, False, ['item1', 'item2', 'item12']),
    (['file10.txt', 'file2.txt', 'file1.txt'], lambda x: x.split('.')[-1], False, ['file1.txt', 'file2.txt', 'file10.txt']),
    (['apple10', 'apple2', 'apple1'], None, True, ['apple10', 'apple2', 'apple1'])
])
def test_invalid_input(to_sort, key, reverse, expected):
    result = naturally(to_sort, key, reverse)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_sorting_naturally_0_test_invalid_input.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
____________ test_invalid_input[to_sort1-<lambda>-False-expected1] _____________

to_sort = ['file10.txt', 'file2.txt', 'file1.txt']
key = <function <lambda> at 0x7ff635c4bb00>, reverse = False
expected = ['file1.txt', 'file2.txt', 'file10.txt']

    @pytest.mark.parametrize("to_sort, key, reverse, expected", [
        (['item12', 'item2', 'item1'], None, False, ['item1', 'item2', 'item12']),
        (['file10.txt', 'file2.txt', 'file1.txt'], lambda x: x.split('.')[-1], False, ['file1.txt', 'file2.txt', 'file10.txt']),
        (['apple10', 'apple2', 'apple1'], None, True, ['apple10', 'apple2', 'apple1'])
    ])
    def test_invalid_input(to_sort, key, reverse, expected):
        result = naturally(to_sort, key, reverse)
>       assert result == expected
E       AssertionError: assert ['file10.txt'..., 'file1.txt'] == ['file1.txt',... 'file10.txt']
E         
E         At index 0 diff: 'file10.txt' != 'file1.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_sorting_naturally_0_test_invalid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting_naturally_0_test_invalid_input.py::test_invalid_input[to_sort1-<lambda>-False-expected1]
========================= 1 failed, 2 passed in 0.11s ==========================
"""