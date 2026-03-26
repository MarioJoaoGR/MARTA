
import pytest
from docstring_parser import parse
import typing as T

def test_default_args(
    source: str,
    expected_is_optional: bool,
    expected_type_name: T.Optional[str],
    expected_default: T.Optional[str],
) -> None:
    """Test parsing default arguments."""
    docstring = parse(source)
    assert docstring is not None
    assert len(docstring.params) == 1

    arg1 = docstring.params[0]
    assert arg1.is_optional == expected_is_optional
    assert arg1.type_name == expected_type_name
    assert arg1.default == expected_default

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_edge_case_none_as_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_edge_case_none_as_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""