
import pytest
from isort._vendored.tomli._parser import parse_key, TOML_WS
from typing import Tuple, Optional, List

Key = Tuple[str, ...]
Pos = int

def skip_chars(src: str, pos: Pos, chars: str) -> Pos:
    while pos < len(src) and src[pos] in chars:
        pos += 1
    return pos

def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, str]:
    if src[pos].isalpha():
        start = pos
        while pos < len(src) and (src[pos].isalnum() or src[pos] == '_'):
            pos += 1
        return pos, src[start:pos]
    elif src[pos] in '"\'':
        quote_char = src[pos]
        pos += 1
        start = pos
        while pos < len(src) and src[pos] != quote_char:
            if src[pos] == '\\' and pos + 1 < len(src):
                pos += 1
            pos += 1
        return pos, src[start:pos]
    else:
        raise ValueError(f"Invalid initial character for a key part (at line {1}, column {pos - start})")

@pytest.mark.parametrize("src, expected_pos, expected_key", [
    ("key", 3, ("key",)),
    ("a.b.c", 7, ("a", "b", "c")),
    ('"hello".world', 14, ('hello', 'world')),
])
def test_valid_key_nested(src: str, expected_pos: int, expected_key: Key):
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert new_pos == expected_pos

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_nested.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________ test_valid_key_nested[a.b.c-7-expected_key1] _________________

src = 'a.b.c', expected_pos = 7, expected_key = ('a', 'b', 'c')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("key", 3, ("key",)),
        ("a.b.c", 7, ("a", "b", "c")),
        ('"hello".world', 14, ('hello', 'world')),
    ])
    def test_valid_key_nested(src: str, expected_pos: int, expected_key: Key):
        pos = 0
        new_pos, key = parse_key(src, pos)
>       assert new_pos == expected_pos
E       assert 5 == 7

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_nested.py:40: AssertionError
____________ test_valid_key_nested["hello".world-14-expected_key2] _____________

src = '"hello".world', expected_pos = 14, expected_key = ('hello', 'world')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("key", 3, ("key",)),
        ("a.b.c", 7, ("a", "b", "c")),
        ('"hello".world', 14, ('hello', 'world')),
    ])
    def test_valid_key_nested(src: str, expected_pos: int, expected_key: Key):
        pos = 0
        new_pos, key = parse_key(src, pos)
>       assert new_pos == expected_pos
E       assert 13 == 14

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_nested.py:40: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_nested.py::test_valid_key_nested[a.b.c-7-expected_key1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_nested.py::test_valid_key_nested["hello".world-14-expected_key2]
========================= 2 failed, 1 passed in 0.11s ==========================
"""