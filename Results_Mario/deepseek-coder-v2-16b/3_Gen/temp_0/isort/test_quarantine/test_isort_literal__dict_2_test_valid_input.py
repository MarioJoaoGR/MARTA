
from unittest.mock import MagicMock
import pytest
from isort.literal import _dict

def test_valid_input():
    # Create a mock for ISortPrettyPrinter
    printer = MagicMock()
    
    # Define the dictionary to be sorted and formatted
    value = {'a': 3, 'b': 1, 'c': 2}
    
    # Call the function with the mocked printer
    result = _dict(value, printer)
    
    # Ensure that the dictionary is sorted by its values before formatting
    assert list(sorted(value.items())) == [('b', 1), ('c', 2), ('a', 3)]
    
    # Check if the pretty printer's pformat method was called with the correct argument
    expected_formatted_dict = {k: v for k, v in sorted(value.items())}
    printer.pformat.assert_called_with(expected_formatted_dict)

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

isort/Test4DT_tests/test_isort_literal__dict_2_test_valid_input.py F     [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock for ISortPrettyPrinter
        printer = MagicMock()
    
        # Define the dictionary to be sorted and formatted
        value = {'a': 3, 'b': 1, 'c': 2}
    
        # Call the function with the mocked printer
        result = _dict(value, printer)
    
        # Ensure that the dictionary is sorted by its values before formatting
>       assert list(sorted(value.items())) == [('b', 1), ('c', 2), ('a', 3)]
E       AssertionError: assert [('a', 3), ('b', 1), ('c', 2)] == [('b', 1), ('c', 2), ('a', 3)]
E         
E         At index 0 diff: ('a', 3) != ('b', 1)
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_literal__dict_2_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal__dict_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.13s ===============================
"""