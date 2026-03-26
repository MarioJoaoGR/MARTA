
import pytest
from isort._vendored.tomli._parser import parse_key, TOMLDecodeError
from isort._vendor.tomli._parser import Pos, Key

def test_edge_case_empty_input():
    src = ""
    pos = Pos(0)
    
    with pytest.raises(TOMLDecodeError):
        new_pos, parsed_key = parse_key(src, pos)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_key_0_test_edge_case_empty_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_0_test_edge_case_empty_input.py:4:0: E0401: Unable to import 'isort._vendor.tomli._parser' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_0_test_edge_case_empty_input.py:4:0: E0611: No name '_vendor' in module 'isort' (no-name-in-module)


"""