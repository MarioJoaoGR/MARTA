
import pytest
from flutes.iterator import split_by

def test_valid_input_basic():
    # Test case 1: Splitting a list of integers by even numbers
    result = list(split_by([1, 2, 3, 4, 5], criterion=lambda x: x % 2 == 0))
    assert result == [[1, 3, 5], [2, 4]]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_basic.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_basic ____________________________

    def test_valid_input_basic():
        # Test case 1: Splitting a list of integers by even numbers
        result = list(split_by([1, 2, 3, 4, 5], criterion=lambda x: x % 2 == 0))
>       assert result == [[1, 3, 5], [2, 4]]
E       assert [[1], [3], [5]] == [[1, 3, 5], [2, 4]]
E         
E         At index 0 diff: [1] != [1, 3, 5]
E         Left contains one more item: [5]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_basic.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_valid_input_basic.py::test_valid_input_basic
============================== 1 failed in 0.10s ===============================
"""