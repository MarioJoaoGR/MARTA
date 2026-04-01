
import pytest
from isort._vendored.tomli._parser import parse_value, suffixed_err
from isort._vendored.tomli._shared_types import Pos
from typing import Tuple, Any, Optional

@pytest.mark.parametrize("src", ['Hello "world"'])
def test_valid_basic_string(src):
    pos = 0
    parsed_value, new_pos = parse_value(src, Pos(pos), float)
    assert parsed_value == 'Hello "world"'
    assert new_pos == len('Hello "world"')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_value_2_test_valid_basic_string
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_2_test_valid_basic_string.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_2_test_valid_basic_string.py:4:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)


"""