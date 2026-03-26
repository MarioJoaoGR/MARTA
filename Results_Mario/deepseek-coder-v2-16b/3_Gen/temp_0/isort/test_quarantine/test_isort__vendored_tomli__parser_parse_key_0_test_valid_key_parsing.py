
import pytest
from isort._vendored.tomli._parser import parse_key, Pos, Key, BARE_KEY_CHARS, TOML_WS, parse_key_part, parse_literal_str, parse_one_line_basic_str, suffixed_err

@pytest.mark.parametrize("src, expected_pos, expected_key", [
    ("a.b.c", 5, ('a', 'b', 'c')),
    (" a. b . c ", 7, ('a', 'b', 'c')),
    (".a.b.c", 1, ('a', 'b', 'c')),
    ("a.b.c.", 5, ('a', 'b', 'c')),
])
def test_valid_key_parsing(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
    pos = Pos(0)
    new_pos, parsed_key = parse_key(src, pos)
    assert new_pos.get() == expected_pos
    assert parsed_key == expected_key

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_key_0_test_valid_key_parsing
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_0_test_valid_key_parsing.py:11:70: E0602: Undefined variable 'Tuple' (undefined-variable)


"""