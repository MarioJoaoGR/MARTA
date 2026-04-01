
import pytest
from docstring_parser import parse, DocstringStyle
from docstring_parser.exceptions import ParseError

def test_autodetection_error_detection() -> None:
    """Test autodection for the case where one of the parsers throws an error
    and another one succeeds.
    """
    source = """
    Does something useless

    :param 3 + 3 a: a param
    """

    with pytest.raises(ParseError):
        # assert that one of the parsers does raise
        parse(source, DocstringStyle.REST)

    # assert that autodetection still works
    docstring = parse(source)

    assert docstring
    assert docstring.style == DocstringStyle.GOOGLE

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parser_test_autodetection_error_detection_2_test_edge_case
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_autodetection_error_detection_2_test_edge_case.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_autodetection_error_detection_2_test_edge_case.py:3:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_autodetection_error_detection_2_test_edge_case.py:4:0: E0401: Unable to import 'docstring_parser.exceptions' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_autodetection_error_detection_2_test_edge_case.py:4:0: E0611: No name 'exceptions' in module 'docstring_parser' (no-name-in-module)


"""