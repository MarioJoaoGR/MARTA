
import pytest
import itertools
from docstring_parser.numpydoc import _pairwise

def test_valid_input():
    # Test case 1: Standard list of integers
    iterable = [1, 2, 3, 4]
    expected_output = [(1, 2), (2, 3), (3, 4)]
    result = list(_pairwise(iterable))
    assert result == expected_output

    # Test case 2: List with fewer than two elements
    iterable = [1]
    expected_output = []
    result = list(_pairwise(iterable))
    assert result == expected_output

    # Test case 3: List with an odd number of elements, using the default end value
    iterable = [1, 2, 3]
    expected_output = [(1, 2), (2, 3)]
    result = list(_pairwise(iterable))
    assert result == expected_output

    # Test case 4: List with an odd number of elements, using a custom end value
    iterable = [1, 2, 3]
    end_value = 'end'
    expected_output = [(1, 2), (2, 3)]
    result = list(_pairwise(iterable, end=end_value))
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
        # Test case 1: Standard list of integers
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
============================== 1 failed in 0.03s ===============================
"""