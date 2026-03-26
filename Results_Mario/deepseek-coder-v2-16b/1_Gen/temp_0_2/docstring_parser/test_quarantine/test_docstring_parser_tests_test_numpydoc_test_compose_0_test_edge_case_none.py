
from docstring_parser.tests.test_numpydoc import Docstring
import pytest

def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    parsed_docstring = parse(source)
    assert compose(parsed_docstring) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_compose_0_test_edge_case_none
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_0_test_edge_case_none.py:2:0: E0611: No name 'Docstring' in module 'docstring_parser.tests.test_numpydoc' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_0_test_edge_case_none.py:7:23: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_0_test_edge_case_none.py:8:11: E0602: Undefined variable 'compose' (undefined-variable)


"""