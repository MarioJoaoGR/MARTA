
import pytest
from src import parse_literal_str, Pos

def test_none_input():
    with pytest.raises(ValueError):
        parse_literal_str(src=None, pos=Pos())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_literal_str_0_test_none_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_none_input.py:3:0: E0401: Unable to import 'src' (import-error)


"""