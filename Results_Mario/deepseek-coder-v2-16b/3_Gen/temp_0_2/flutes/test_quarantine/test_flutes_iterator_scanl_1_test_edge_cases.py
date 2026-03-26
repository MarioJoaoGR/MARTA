
import pytest
from flutes.iterator import scanl
from operator import add

@pytest.mark.parametrize("func, iterable, initial, expected", [
    (add, None, 0, TypeError),  # Test with None as iterable
    (add, [], 0, []),            # Test with empty list
    (add, [1, 2, 3], None, TypeError),  # Test with None as initial value
    (lambda x, y: x * y, [1, 2, 3], 1, [1, 1, 2, 6]),  # Test with a different function
])
def test_edge_cases(func, iterable, initial, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            list(scanl(func, iterable, initial))
    else:
        assert list(scanl(func, iterable, initial)) == expected

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

flutes/Test4DT_tests/test_flutes_iterator_scanl_1_test_edge_cases.py .F. [ 75%]
.                                                                        [100%]

=================================== FAILURES ===================================
__________________ test_edge_cases[add-iterable1-0-expected1] __________________

func = <built-in function add>, iterable = [], initial = 0, expected = []

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, None, 0, TypeError),  # Test with None as iterable
        (add, [], 0, []),            # Test with empty list
        (add, [1, 2, 3], None, TypeError),  # Test with None as initial value
        (lambda x, y: x * y, [1, 2, 3], 1, [1, 1, 2, 6]),  # Test with a different function
    ])
    def test_edge_cases(func, iterable, initial, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                list(scanl(func, iterable, initial))
        else:
>           assert list(scanl(func, iterable, initial)) == expected
E           assert [0] == []
E             
E             Left contains one more item: 0
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanl_1_test_edge_cases.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_1_test_edge_cases.py::test_edge_cases[add-iterable1-0-expected1]
========================= 1 failed, 3 passed in 0.09s ==========================
"""