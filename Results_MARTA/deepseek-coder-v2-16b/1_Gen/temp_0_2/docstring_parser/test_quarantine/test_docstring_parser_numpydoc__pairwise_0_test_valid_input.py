
import pytest
import itertools
from docstring_parser.numpydoc import _pairwise

def test_valid_input():
    # Test case 1: List of numbers
    iterable = [1, 2, 3, 4]
    expected_output = [(1, 2), (2, 3), (3, 4)]
    result = list(_pairwise(iterable))
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__pairwise_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case 1: List of numbers
        iterable = [1, 2, 3, 4]
        expected_output = [(1, 2), (2, 3), (3, 4)]
        result = list(_pairwise(iterable))
>       assert result == expected_output
E       assert [(1, 2), (2, ...4), (4, None)] == [(1, 2), (2, 3), (3, 4)]
E         
E         Left contains one more item: (4, None)
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__pairwise_0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc__pairwise_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""