
from isort.literal import _unique_tuple
from unittest.mock import Mock
import pytest

def test_valid_input():
    # Create a mock pretty printer
    printer = Mock()
    
    # Define the expected output for the unique and sorted tuple (3, 1, 2)
    value = (3, 1, 2, 2, 3)
    result = _unique_tuple(value, printer)
    
    # Assert that the result matches the expected format "['1', '2', '3']"
    assert result == "['1', '2', '3']"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_literal__unique_tuple_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock pretty printer
        printer = Mock()
    
        # Define the expected output for the unique and sorted tuple (3, 1, 2)
        value = (3, 1, 2, 2, 3)
        result = _unique_tuple(value, printer)
    
        # Assert that the result matches the expected format "['1', '2', '3']"
>       assert result == "['1', '2', '3']"
E       assert <Mock name='mock.pformat()' id='140558694483024'> == "['1', '2', '3']"

isort/Test4DT_tests/test_isort_literal__unique_tuple_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal__unique_tuple_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""