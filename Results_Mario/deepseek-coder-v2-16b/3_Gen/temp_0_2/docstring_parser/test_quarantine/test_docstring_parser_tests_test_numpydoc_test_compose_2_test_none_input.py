
from docstring_parser.parsers import parse
from docstring_parser.tests.test_numpydoc import compose

def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    assert compose(parse(source)) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_compose_2_test_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_2_test_none_input.py:2:0: E0401: Unable to import 'docstring_parser.parsers' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_2_test_none_input.py:2:0: E0611: No name 'parsers' in module 'docstring_parser' (no-name-in-module)


"""