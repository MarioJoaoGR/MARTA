
from isort._vendored.tomli._parser import parse_key, parse_value, skip_chars
from isort._vendored.tomli._shared_types import Pos, Key, Any, ParseFloat, suffixed_err
from typing import Tuple, Optional

def parse_key_value_pair(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, Key, Any]:
    pos, key = parse_key(src, pos)
    try:
        char: Optional[str] = src[pos]
    except IndexError:
        char = None
    if char != "=":
        raise suffixed_err(src, pos, 'Expected "=" after a key in a key/value pair')
    pos += 1
    pos = skip_chars(src, pos, TOML_WS)
    pos, value = parse_value(src, pos, parse_float)
    return pos, key, value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_invalid_input.py:3:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_invalid_input.py:3:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_invalid_input.py:15:31: E0602: Undefined variable 'TOML_WS' (undefined-variable)


"""