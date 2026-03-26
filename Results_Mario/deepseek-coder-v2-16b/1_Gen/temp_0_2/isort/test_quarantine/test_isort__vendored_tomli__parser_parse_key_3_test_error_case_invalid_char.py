
from typing import Tuple
from isort._vendored.tomli._parser import parse_key, Pos, Key
import pytest

def skip_chars(src: str, pos: int, chars: str) -> int:
    while pos < len(src) and src[pos] in chars:
        pos += 1
    return pos

TOML_WS = " \t\n"

@pytest.mark.parametrize("src, expected_pos, expected_key", [
    ("name", Pos(0), ("name",)),
    ("'name'", Pos(0), ("name",)),
    ('"name"', Pos(0), ("name",)),
    ("name.last", Pos(0), ("name", "last")),
    ("name.'last'", Pos(0), ("name", "last")),
    ("name.\"last\"", Pos(0), ("name", "last")),
])
def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
    pos = Pos(expected_pos)
    actual_pos, actual_key = parse_key(src, pos)
    assert actual_pos == expected_pos
    assert actual_key == expected_key

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_____________________ test_parse_key[name-0-expected_key0] _____________________

src = 'name', expected_pos = 0, expected_key = ('name',)

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("name", Pos(0), ("name",)),
        ("'name'", Pos(0), ("name",)),
        ('"name"', Pos(0), ("name",)),
        ("name.last", Pos(0), ("name", "last")),
        ("name.'last'", Pos(0), ("name", "last")),
        ("name.\"last\"", Pos(0), ("name", "last")),
    ])
    def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
        pos = Pos(expected_pos)
        actual_pos, actual_key = parse_key(src, pos)
>       assert actual_pos == expected_pos
E       assert 4 == 0

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py:24: AssertionError
____________________ test_parse_key['name'-0-expected_key1] ____________________

src = "'name'", expected_pos = 0, expected_key = ('name',)

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("name", Pos(0), ("name",)),
        ("'name'", Pos(0), ("name",)),
        ('"name"', Pos(0), ("name",)),
        ("name.last", Pos(0), ("name", "last")),
        ("name.'last'", Pos(0), ("name", "last")),
        ("name.\"last\"", Pos(0), ("name", "last")),
    ])
    def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
        pos = Pos(expected_pos)
        actual_pos, actual_key = parse_key(src, pos)
>       assert actual_pos == expected_pos
E       assert 6 == 0

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py:24: AssertionError
____________________ test_parse_key["name"-0-expected_key2] ____________________

src = '"name"', expected_pos = 0, expected_key = ('name',)

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("name", Pos(0), ("name",)),
        ("'name'", Pos(0), ("name",)),
        ('"name"', Pos(0), ("name",)),
        ("name.last", Pos(0), ("name", "last")),
        ("name.'last'", Pos(0), ("name", "last")),
        ("name.\"last\"", Pos(0), ("name", "last")),
    ])
    def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
        pos = Pos(expected_pos)
        actual_pos, actual_key = parse_key(src, pos)
>       assert actual_pos == expected_pos
E       assert 6 == 0

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py:24: AssertionError
__________________ test_parse_key[name.last-0-expected_key3] ___________________

src = 'name.last', expected_pos = 0, expected_key = ('name', 'last')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("name", Pos(0), ("name",)),
        ("'name'", Pos(0), ("name",)),
        ('"name"', Pos(0), ("name",)),
        ("name.last", Pos(0), ("name", "last")),
        ("name.'last'", Pos(0), ("name", "last")),
        ("name.\"last\"", Pos(0), ("name", "last")),
    ])
    def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
        pos = Pos(expected_pos)
        actual_pos, actual_key = parse_key(src, pos)
>       assert actual_pos == expected_pos
E       assert 9 == 0

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py:24: AssertionError
_________________ test_parse_key[name.'last'-0-expected_key4] __________________

src = "name.'last'", expected_pos = 0, expected_key = ('name', 'last')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("name", Pos(0), ("name",)),
        ("'name'", Pos(0), ("name",)),
        ('"name"', Pos(0), ("name",)),
        ("name.last", Pos(0), ("name", "last")),
        ("name.'last'", Pos(0), ("name", "last")),
        ("name.\"last\"", Pos(0), ("name", "last")),
    ])
    def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
        pos = Pos(expected_pos)
        actual_pos, actual_key = parse_key(src, pos)
>       assert actual_pos == expected_pos
E       assert 11 == 0

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py:24: AssertionError
_________________ test_parse_key[name."last"-0-expected_key5] __________________

src = 'name."last"', expected_pos = 0, expected_key = ('name', 'last')

    @pytest.mark.parametrize("src, expected_pos, expected_key", [
        ("name", Pos(0), ("name",)),
        ("'name'", Pos(0), ("name",)),
        ('"name"', Pos(0), ("name",)),
        ("name.last", Pos(0), ("name", "last")),
        ("name.'last'", Pos(0), ("name", "last")),
        ("name.\"last\"", Pos(0), ("name", "last")),
    ])
    def test_parse_key(src: str, expected_pos: int, expected_key: Tuple[str, ...]):
        pos = Pos(expected_pos)
        actual_pos, actual_key = parse_key(src, pos)
>       assert actual_pos == expected_pos
E       assert 11 == 0

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py::test_parse_key[name-0-expected_key0]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py::test_parse_key['name'-0-expected_key1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py::test_parse_key["name"-0-expected_key2]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py::test_parse_key[name.last-0-expected_key3]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py::test_parse_key[name.'last'-0-expected_key4]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_3_test_error_case_invalid_char.py::test_parse_key[name."last"-0-expected_key5]
============================== 6 failed in 0.13s ===============================
"""