
from docstring_parser import parse

def test_meta_with_args() -> None:
    """Test parsing meta with additional arguments."""
    docstring = parse(
        """
        Short description

        @meta ene due rabe: asd
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["ene", "due", "rabe"]
    assert docstring.meta[0].description == "asd"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_meta_with_args_1_test_missing_lines
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_with_args_1_test_missing_lines.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""