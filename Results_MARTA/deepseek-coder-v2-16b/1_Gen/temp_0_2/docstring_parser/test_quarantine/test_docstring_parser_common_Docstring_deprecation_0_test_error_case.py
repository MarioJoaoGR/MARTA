
import pytest
from docstring_parser.common import Docstring, DocstringStyle, DocstringMeta, DocstringDeprecated

def test_deprecation():
    # Create a Docstring instance without any deprecation meta
    docstring = Docstring()
    assert docstring.deprecation() is None

    # Create a Docstring instance with a deprecation meta
    docstring = Docstring(meta=[DocstringDeprecated("This function is deprecated.")])
    assert isinstance(docstring.deprecation(), DocstringDeprecated)
    assert docstring.deprecation().message == "This function is deprecated."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_Docstring_deprecation_0_test_error_case
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_deprecation_0_test_error_case.py:8:11: E1102: docstring.deprecation is not callable (not-callable)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_deprecation_0_test_error_case.py:11:16: E1123: Unexpected keyword argument 'meta' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_deprecation_0_test_error_case.py:11:32: E1120: No value for argument 'description' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_deprecation_0_test_error_case.py:11:32: E1120: No value for argument 'version' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_deprecation_0_test_error_case.py:12:22: E1102: docstring.deprecation is not callable (not-callable)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_deprecation_0_test_error_case.py:13:11: E1102: docstring.deprecation is not callable (not-callable)


"""