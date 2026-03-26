
# Module: docstring_parser.tests.test_google
# Import the function using its provided module name.
from docstring_parser.tests.test_google import test_meta_with_multiline_description

def test_meta_with_multiline_description():
    """Test parsing multiline meta documentation."""
    # Call the function to get the parsed docstring object.
    from docstring_parser import parse  # Importing inside the function to avoid undefined variable error
    
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
    
    # Assert that the short description matches the expected value.
    assert docstring.short_description == "Short description"
    
    # Assert that there is exactly one meta entry.
    assert len(docstring.meta) == 1
    
    # Assert that the argument name and type are correct.
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    
    # Assert that the description of the parameter is as expected.
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_meta_with_multiline_description_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_with_multiline_description_0.py:6:0: E0102: function already defined line 4 (function-redefined)

"""