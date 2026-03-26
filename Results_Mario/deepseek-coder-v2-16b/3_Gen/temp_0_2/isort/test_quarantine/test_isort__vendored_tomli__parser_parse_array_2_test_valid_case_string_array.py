
import pytest
from isort._vendored.tomli._parser import parse_array, Pos, ParseFloat

def test_valid_case_string_array():
    src = "[\"apple\", \"banana\", \"cherry\"]"
    pos = 0
    parse_float = None

    result: Tuple[Pos, List] = parse_array(src, pos, parse_float)

    assert result == (28, ["apple", "banana", "cherry"])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_array_2_test_valid_case_string_array
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_2_test_valid_case_string_array.py:10:12: E0602: Undefined variable 'Tuple' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_2_test_valid_case_string_array.py:10:23: E0602: Undefined variable 'List' (undefined-variable)


"""