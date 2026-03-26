
# Module: docstring_parser.tests.test_epydoc
import pytest
from your_module import test_meta_with_multiline_description

def test_meta_with_multiline_description():
    """Test parsing multiline meta documentation."""
    from your_module import parse  # Importing here to resolve the pylint error about undefined variable

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
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_meta_with_multiline_description_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_with_multiline_description_0.py:4:0: E0401: Unable to import 'your_module' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_with_multiline_description_0.py:6:0: E0102: function already defined line 4 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_with_multiline_description_0.py:8:4: E0401: Unable to import 'your_module' (import-error)

"""