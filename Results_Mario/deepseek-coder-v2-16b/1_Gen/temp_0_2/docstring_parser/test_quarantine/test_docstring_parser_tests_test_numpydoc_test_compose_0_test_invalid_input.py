
from docstring_parser.tests.test_numpydoc import Docstring
from docstring_parser.tests.test_numpydoc import compose, parse

def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    assert compose(parse(source)) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_compose_0_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_0_test_invalid_input.py:2:0: E0611: No name 'Docstring' in module 'docstring_parser.tests.test_numpydoc' (no-name-in-module)


"""