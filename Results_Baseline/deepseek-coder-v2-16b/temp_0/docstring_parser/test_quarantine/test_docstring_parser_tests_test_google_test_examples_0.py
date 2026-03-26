
# Module: docstring_parser.tests.test_google
# Import the function from its module
from docstring_parser.tests.test_google import test_examples

def test_examples():
    # Call the function to be tested
    from docstring_parser import parse  # Corrected the import and variable usage
    
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
    
    # Assertions to verify the expected behavior
    assert len(docstring.examples) == 2, "Expected exactly two examples"
    assert docstring.examples[0].description == "example: 1", "The first example should have the description 'example: 1'"
    assert docstring.examples[1].description == "long example\n\nmere here", "The second example should have the description 'long example\\n\\nmere here'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_examples_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_examples_0.py:6:0: E0102: function already defined line 4 (function-redefined)

"""