
import pytest
from isort._vendored.tomli._parser import parse_key, Pos, TOML_WS, Key

@pytest.mark.parametrize("src, expected_pos, expected_key", [
    ("a.b.c", 5, ('a', 'b', 'c')),
    (" a. b .c", 7, ('a', 'b', 'c')),
    (".a.b.c", 1, ('a', 'b', 'c')),
    ("a.b.c ", 5, ('a', 'b', 'c')),
    ("a.b.c.", 6, ('a', 'b', 'c')),
])
def test_valid_key_parsing(src: str, expected_pos: int, expected_key: Key):
    pos = Pos(0)
    new_pos, parsed_key = parse_key(src, pos)
    assert new_pos == expected_pos
    assert parsed_key == expected_key

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py . [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_______________ test_valid_key_parsing[ a. b .c-7-expected_key1] _______________

src = ' a. b .c', expected_pos = 7, expected_key = ('a', 'b', 'c')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("a.b.c", 5, ('a', 'b', 'c')),
        (" a. b .c", 7, ('a', 'b', 'c')),
        (".a.b.c", 1, ('a', 'b', 'c')),
        ("a.b.c ", 5, ('a', 'b', 'c')),
        ("a.b.c.", 6, ('a', 'b', 'c')),
    ])
    def test_valid_key_parsing(src: str, expected_pos: int, expected_key: Key):
        pos = Pos(0)
>       new_pos, parsed_key = parse_key(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:358: in parse_key
    pos, key_part = parse_key_part(src, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = ' a. b .c', pos = 0

    def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, str]:
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char in BARE_KEY_CHARS:
            start_pos = pos
            pos = skip_chars(src, pos, BARE_KEY_CHARS)
            return pos, src[start_pos:pos]
        if char == "'":
            return parse_literal_str(src, pos)
        if char == '"':
            return parse_one_line_basic_str(src, pos)
>       raise suffixed_err(src, pos, "Invalid initial character for a key part")
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid initial character for a key part (at line 1, column 1)

isort/isort/_vendored/tomli/_parser.py:388: TOMLDecodeError
________________ test_valid_key_parsing[.a.b.c-1-expected_key2] ________________

src = '.a.b.c', expected_pos = 1, expected_key = ('a', 'b', 'c')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("a.b.c", 5, ('a', 'b', 'c')),
        (" a. b .c", 7, ('a', 'b', 'c')),
        (".a.b.c", 1, ('a', 'b', 'c')),
        ("a.b.c ", 5, ('a', 'b', 'c')),
        ("a.b.c.", 6, ('a', 'b', 'c')),
    ])
    def test_valid_key_parsing(src: str, expected_pos: int, expected_key: Key):
        pos = Pos(0)
>       new_pos, parsed_key = parse_key(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:358: in parse_key
    pos, key_part = parse_key_part(src, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '.a.b.c', pos = 0

    def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, str]:
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char in BARE_KEY_CHARS:
            start_pos = pos
            pos = skip_chars(src, pos, BARE_KEY_CHARS)
            return pos, src[start_pos:pos]
        if char == "'":
            return parse_literal_str(src, pos)
        if char == '"':
            return parse_one_line_basic_str(src, pos)
>       raise suffixed_err(src, pos, "Invalid initial character for a key part")
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid initial character for a key part (at line 1, column 1)

isort/isort/_vendored/tomli/_parser.py:388: TOMLDecodeError
________________ test_valid_key_parsing[a.b.c -5-expected_key3] ________________

src = 'a.b.c ', expected_pos = 5, expected_key = ('a', 'b', 'c')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("a.b.c", 5, ('a', 'b', 'c')),
        (" a. b .c", 7, ('a', 'b', 'c')),
        (".a.b.c", 1, ('a', 'b', 'c')),
        ("a.b.c ", 5, ('a', 'b', 'c')),
        ("a.b.c.", 6, ('a', 'b', 'c')),
    ])
    def test_valid_key_parsing(src: str, expected_pos: int, expected_key: Key):
        pos = Pos(0)
        new_pos, parsed_key = parse_key(src, pos)
>       assert new_pos == expected_pos
E       assert 6 == 5

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py:15: AssertionError
________________ test_valid_key_parsing[a.b.c.-6-expected_key4] ________________

src = 'a.b.c.', expected_pos = 6, expected_key = ('a', 'b', 'c')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("a.b.c", 5, ('a', 'b', 'c')),
        (" a. b .c", 7, ('a', 'b', 'c')),
        (".a.b.c", 1, ('a', 'b', 'c')),
        ("a.b.c ", 5, ('a', 'b', 'c')),
        ("a.b.c.", 6, ('a', 'b', 'c')),
    ])
    def test_valid_key_parsing(src: str, expected_pos: int, expected_key: Key):
        pos = Pos(0)
>       new_pos, parsed_key = parse_key(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:370: in parse_key
    pos, key_part = parse_key_part(src, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'a.b.c.', pos = 6

    def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, str]:
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char in BARE_KEY_CHARS:
            start_pos = pos
            pos = skip_chars(src, pos, BARE_KEY_CHARS)
            return pos, src[start_pos:pos]
        if char == "'":
            return parse_literal_str(src, pos)
        if char == '"':
            return parse_one_line_basic_str(src, pos)
>       raise suffixed_err(src, pos, "Invalid initial character for a key part")
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid initial character for a key part (at end of document)

isort/isort/_vendored/tomli/_parser.py:388: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py::test_valid_key_parsing[ a. b .c-7-expected_key1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py::test_valid_key_parsing[.a.b.c-1-expected_key2]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py::test_valid_key_parsing[a.b.c -5-expected_key3]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_key_parsing.py::test_valid_key_parsing[a.b.c.-6-expected_key4]
========================= 4 failed, 1 passed in 0.18s ==========================
"""