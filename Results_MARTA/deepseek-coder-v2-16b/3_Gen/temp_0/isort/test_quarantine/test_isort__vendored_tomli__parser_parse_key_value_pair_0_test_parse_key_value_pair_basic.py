
from isort._vendored.tomli._parser import parse_key, parse_value, Pos, ParseFloat
from typing import Tuple, Optional, Any

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
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_parse_key_value_pair_basic
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_parse_key_value_pair_basic.py:5:84: E0602: Undefined variable 'Key' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_parse_key_value_pair_basic.py:12:14: E0602: Undefined variable 'suffixed_err' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_parse_key_value_pair_basic.py:14:10: E0602: Undefined variable 'skip_chars' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_parse_key_value_pair_basic.py:14:31: E0602: Undefined variable 'TOML_WS' (undefined-variable)


"""