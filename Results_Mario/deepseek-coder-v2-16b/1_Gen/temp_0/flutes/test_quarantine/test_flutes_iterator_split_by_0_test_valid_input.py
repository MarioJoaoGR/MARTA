
import pytest
from flutes.iterator import split_by

def test_valid_input():
    def is_even(n: int) -> bool: return n % 2 == 0
    
    iterable1 = [1, 2, 3, 4, 5]
    expected1 = [[1, 3, 5], [2, 4]]
    result1 = list(split_by(iterable1, criterion=is_even))
    assert result1 == expected1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def is_even(n: int) -> bool: return n % 2 == 0
    
        iterable1 = [1, 2, 3, 4, 5]
        expected1 = [[1, 3, 5], [2, 4]]
        result1 = list(split_by(iterable1, criterion=is_even))
>       assert result1 == expected1
E       assert [[1], [3], [5]] == [[1, 3, 5], [2, 4]]
E         
E         At index 0 diff: [1] != [1, 3, 5]
E         Left contains one more item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""