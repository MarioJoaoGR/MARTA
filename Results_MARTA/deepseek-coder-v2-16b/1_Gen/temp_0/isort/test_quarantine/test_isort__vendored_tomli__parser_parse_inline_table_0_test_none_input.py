
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err
from isort._vendored.tomli._shared_types import Pos, ParseFloat, TOML_WS
from isort._vendored.tomli._nested_dict import NestedDict, Flags

def test_none_input():
    with pytest.raises(TypeError):
        parse_inline_table("key1=value1 key2={} key3=3.14}", 0, float)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_inline_table_0_test_none_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_none_input.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_none_input.py:4:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_none_input.py:5:0: E0401: Unable to import 'isort._vendored.tomli._nested_dict' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_none_input.py:5:0: E0611: No name '_nested_dict' in module 'isort._vendored.tomli' (no-name-in-module)


"""