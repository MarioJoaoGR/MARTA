
assert 'short_description' in parsed_result, "Expected short description is missing"
assert 'long_description' not in parsed_result, "Unexpected long description found"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parser_test_short_description_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0.py:2:30: E0602: Undefined variable 'parsed_result' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0.py:3:33: E0602: Undefined variable 'parsed_result' (undefined-variable)

"""