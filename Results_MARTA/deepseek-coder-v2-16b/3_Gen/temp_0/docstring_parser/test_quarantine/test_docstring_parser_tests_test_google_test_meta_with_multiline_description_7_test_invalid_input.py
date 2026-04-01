
import pytest
from docstring_parser import parse

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    docstring = parse(
        """
        Short description

        Args:
            spam: asd
                1
                    2
                3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_meta_with_multiline_description_7_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_with_multiline_description_7_test_invalid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""