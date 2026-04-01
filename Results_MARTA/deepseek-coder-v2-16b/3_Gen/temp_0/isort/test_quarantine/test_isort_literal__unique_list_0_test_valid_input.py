
from unittest.mock import Mock
import pytest
from isort.literal import _unique_list, ISortPrettyPrinter

def test_valid_input():
    # Create a mock printer instance
    mock_printer = Mock(spec=ISortPrettyPrinter)
    
    # Define the input list and expected output
    value = [3, 1, 2, 2, 3]
    expected_output = "['1', '2', '3']"
    
    # Call the function with the mock printer
    result = _unique_list(value, mock_printer)
    
    # Assert that the output matches the expected value
    assert result == expected_output

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

isort/Test4DT_tests/test_isort_literal__unique_list_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock printer instance
        mock_printer = Mock(spec=ISortPrettyPrinter)
    
        # Define the input list and expected output
        value = [3, 1, 2, 2, 3]
        expected_output = "['1', '2', '3']"
    
        # Call the function with the mock printer
        result = _unique_list(value, mock_printer)
    
        # Assert that the output matches the expected value
>       assert result == expected_output
E       assert <Mock name='mock.pformat()' id='139635267547536'> == "['1', '2', '3']"

isort/Test4DT_tests/test_isort_literal__unique_list_0_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal__unique_list_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.12s ===============================
"""