
# Module: docstring_parser.tests.test_epydoc
# test_epydoc.py
import pytest
from your_module_name import parse  # Replace 'your_module_name' with the actual module name

def test_multiple_meta():
    """Test parsing multiple meta."""
    docstring = parse(
        """
        Short description

        @meta1: asd
            1
                2
            3
        @meta2: herp
        @meta3: derp
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 3
    assert docstring.meta[0].args == ["meta1"]
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
    assert docstring.meta[1].args == ["meta2"]
    assert docstring.meta[1].description == "herp"
    assert docstring.meta[2].args == ["meta3"]
    assert docstring.meta[2].description == "derp"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_multiple_meta_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_multiple_meta_0.py:5:0: E0401: Unable to import 'your_module_name' (import-error)

"""