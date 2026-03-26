
import pytest
from docstring_parser.tests.test_parser import parse, DocstringStyle

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
************* Module Test4DT_tests.test_docstring_parser_tests_test_parser_test_autodetection_error_detection_0_test_edge_case
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_autodetection_error_detection_0_test_edge_case.py:15:23: E0602: Undefined variable 'ParseError' (undefined-variable)

"""