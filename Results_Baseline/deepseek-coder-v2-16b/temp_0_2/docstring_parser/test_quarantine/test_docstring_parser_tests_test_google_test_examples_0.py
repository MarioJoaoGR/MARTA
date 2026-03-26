
# Module: docstring_parser.tests.test_google
# test_google.py
from docstring_parser.tests.test_google import test_examples

def test_examples():
    """Test parsing examples."""
    from docstring_parser import parse  # Importing inside the function to avoid redefinition error

    docstring = parse(
        """
        Short description
        Example:
            example: 1
        Examples:
            long example

            more here
        """
    )
    assert len(docstring.examples) == 2
    assert docstring.examples[0].description == "example: 1"
    assert docstring.examples[1].description == "long example\n\nmore here"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_examples_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_examples_0.py:6:0: E0102: function already defined line 4 (function-redefined)

"""