
# Module: docstring_parser.tests.test_epydoc
# Import the function from its module
from docstring_parser.tests.test_epydoc import test_short_rtype

def test_short_rtype():
    # Define the input string with a short description and return type information
    string = "Short description.\n\n@rtype: float"
    
    # Parse the docstring
    from docstring_parser import parse
    parsed_docstring = parse(string)
    
    # Assert that the composed docstring matches the original string
    from docstring_parser import compose
    assert compose(parsed_docstring) == string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_short_rtype_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_rtype_0.py:6:0: E0102: function already defined line 4 (function-redefined)

"""