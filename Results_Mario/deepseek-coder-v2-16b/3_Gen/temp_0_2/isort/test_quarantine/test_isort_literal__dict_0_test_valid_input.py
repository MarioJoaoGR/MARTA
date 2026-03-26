
from isort.literal import _dict
from unittest.mock import MagicMock
import pytest

def test_valid_input():
    value = {'a': 3, 'b': 1, 'c': 2}
    printer = MagicMock()
    expected_output = "b: 1, c: 2, a: 3"
    
    # Call the function with the mock and check the output
    result = _dict(value, printer)
    assert result == expected_output
    
    # Verify that the pretty printer's pformat method was called correctly
    sorted_dict = dict(sorted(value.items(), key=lambda item: item[1]))
    printer.pformat.assert_called_once_with(sorted_dict)

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

isort/Test4DT_tests/test_isort_literal__dict_0_test_valid_input.py F     [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        value = {'a': 3, 'b': 1, 'c': 2}
        printer = MagicMock()
        expected_output = "b: 1, c: 2, a: 3"
    
        # Call the function with the mock and check the output
        result = _dict(value, printer)
>       assert result == expected_output
E       AssertionError: assert <MagicMock name='mock.pformat()' id='140108462694608'> == 'b: 1, c: 2, a: 3'

isort/Test4DT_tests/test_isort_literal__dict_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal__dict_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""