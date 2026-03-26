
import pytest
from docstring_parser import parse

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    docstring = parse(
        """
        Short description

        @meta: asd
            1
                2
            3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta"]
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_meta_with_multiline_description_1_test_missing_lines
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_with_multiline_description_1_test_missing_lines.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""