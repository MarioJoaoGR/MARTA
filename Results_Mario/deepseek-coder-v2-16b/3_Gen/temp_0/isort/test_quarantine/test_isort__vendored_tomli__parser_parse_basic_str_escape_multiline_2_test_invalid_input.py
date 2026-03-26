
import pytest
from tomli_w import parse_basic_str_escape_multiline, Pos

def test_invalid_input():
    src = 'This string contains an invalid \x escape sequence'
    with pytest.raises(ValueError):
        parse_basic_str_escape_multiline(src, Pos(0))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_2_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_2_test_invalid_input.py:6:63: E0001: Parsing failed: '(unicode error) 'unicodeescape' codec can't decode bytes in position 32-33: truncated \xXX escape (Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_2_test_invalid_input, line 6)' (syntax-error)


"""