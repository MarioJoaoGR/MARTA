
from docstring_parser.tests.test_google import GoogleParser

def test_invalid_input():
    parser = GoogleParser()
    with pytest.raises(ValueError):
        parser.parse("Invalid Docstring")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_2_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_2_test_invalid_input.py:6:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""