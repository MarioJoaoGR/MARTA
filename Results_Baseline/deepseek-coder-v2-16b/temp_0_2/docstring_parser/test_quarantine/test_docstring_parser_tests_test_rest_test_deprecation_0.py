
# Module: docstring_parser.tests.test_rest
# test_rest.py
from your_module import parse

def test_deprecation():
    """Test parsing deprecation notes."""
    
    # Test case with specified version
    docstring = parse(":deprecation: 1.1.0 this function will be removed")
    assert docstring.deprecation is not None, "Expected deprecation to be parsed but got None"
    assert docstring.deprecation.version == "1.1.0", f"Expected version '1.1.0' but got {docstring.deprecation.version}"
    assert docstring.deprecation.description == "this function will be removed", f"Expected description 'this function will be removed' but got {docstring.deprecation.description}"
    
    # Test case without specified version
    docstring = parse(":deprecation: this function will be removed")
    assert docstring.deprecation is not None, "Expected deprecation to be parsed but got None"
    assert docstring.deprecation.version is None, "Expected version to be None for unspecified version"
    assert docstring.deprecation.description == "this function will be removed", f"Expected description 'this function will be removed' but got {docstring.deprecation.description}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_deprecation_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_deprecation_0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""