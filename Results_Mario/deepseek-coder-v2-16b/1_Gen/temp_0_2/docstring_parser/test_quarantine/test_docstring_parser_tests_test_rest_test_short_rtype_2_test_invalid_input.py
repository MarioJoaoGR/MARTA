
from docstring_parser.tests.test_rest import parse, compose, RenderingStyle

def test_invalid_input():
    string = "Short description.\n\n:rtype: float"
    with pytest.raises(ValueError):
        docstring = parse(string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_short_rtype_2_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_rtype_2_test_invalid_input.py:6:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""