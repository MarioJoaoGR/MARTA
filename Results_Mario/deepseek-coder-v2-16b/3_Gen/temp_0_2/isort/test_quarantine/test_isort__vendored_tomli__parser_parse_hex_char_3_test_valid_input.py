
import pytest
from isort._vendored.tomli._parser import parse_hex_char, suffixed_err, HEXDIGIT_CHARS, Pos, is_unicode_scalar_value

@pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
    ("1a3f", 0, 2, 2, "1"),
    ("1A3F", 0, 2, 2, "1"),
    ("deadbeef", 0, 4, 4, "d"),
    ("cafebabe", 0, 4, 4, "c"),
])
def test_valid_input(src: str, pos: int, hex_len: int, expected_pos: int, expected_char: str):
    new_pos, char = parse_hex_char(src, pos, hex_len)
    assert new_pos == expected_pos
    assert char == expected_char

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_valid_input[1a3f-0-2-2-1] ________________________

src = '1a3f', pos = 0, hex_len = 2, expected_pos = 2, expected_char = '1'

    @pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
        ("1a3f", 0, 2, 2, "1"),
        ("1A3F", 0, 2, 2, "1"),
        ("deadbeef", 0, 4, 4, "d"),
        ("cafebabe", 0, 4, 4, "c"),
    ])
    def test_valid_input(src: str, pos: int, hex_len: int, expected_pos: int, expected_char: str):
        new_pos, char = parse_hex_char(src, pos, hex_len)
        assert new_pos == expected_pos
>       assert char == expected_char
E       AssertionError: assert '\x1a' == '1'
E         
E         - 1
E         + 

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py:14: AssertionError
________________________ test_valid_input[1A3F-0-2-2-1] ________________________

src = '1A3F', pos = 0, hex_len = 2, expected_pos = 2, expected_char = '1'

    @pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
        ("1a3f", 0, 2, 2, "1"),
        ("1A3F", 0, 2, 2, "1"),
        ("deadbeef", 0, 4, 4, "d"),
        ("cafebabe", 0, 4, 4, "c"),
    ])
    def test_valid_input(src: str, pos: int, hex_len: int, expected_pos: int, expected_char: str):
        new_pos, char = parse_hex_char(src, pos, hex_len)
        assert new_pos == expected_pos
>       assert char == expected_char
E       AssertionError: assert '\x1a' == '1'
E         
E         - 1
E         + 

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py:14: AssertionError
______________________ test_valid_input[deadbeef-0-4-4-d] ______________________

src = 'deadbeef', pos = 0, hex_len = 4, expected_pos = 4, expected_char = 'd'

    @pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
        ("1a3f", 0, 2, 2, "1"),
        ("1A3F", 0, 2, 2, "1"),
        ("deadbeef", 0, 4, 4, "d"),
        ("cafebabe", 0, 4, 4, "c"),
    ])
    def test_valid_input(src: str, pos: int, hex_len: int, expected_pos: int, expected_char: str):
>       new_pos, char = parse_hex_char(src, pos, hex_len)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'deadbeef', pos = 4, hex_len = 4

    def parse_hex_char(src: str, pos: Pos, hex_len: int) -> Tuple[Pos, str]:
        hex_str = src[pos : pos + hex_len]
        if len(hex_str) != hex_len or not HEXDIGIT_CHARS.issuperset(hex_str):
            raise suffixed_err(src, pos, "Invalid hex value")
        pos += hex_len
        hex_int = int(hex_str, 16)
        if not is_unicode_scalar_value(hex_int):
>           raise suffixed_err(src, pos, "Escaped character is not a Unicode scalar value")
E           isort._vendored.tomli._parser.TOMLDecodeError: Escaped character is not a Unicode scalar value (at line 1, column 5)

isort/isort/_vendored/tomli/_parser.py:494: TOMLDecodeError
______________________ test_valid_input[cafebabe-0-4-4-c] ______________________

src = 'cafebabe', pos = 0, hex_len = 4, expected_pos = 4, expected_char = 'c'

    @pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
        ("1a3f", 0, 2, 2, "1"),
        ("1A3F", 0, 2, 2, "1"),
        ("deadbeef", 0, 4, 4, "d"),
        ("cafebabe", 0, 4, 4, "c"),
    ])
    def test_valid_input(src: str, pos: int, hex_len: int, expected_pos: int, expected_char: str):
        new_pos, char = parse_hex_char(src, pos, hex_len)
        assert new_pos == expected_pos
>       assert char == expected_char
E       AssertionError: assert '쫾' == 'c'
E         
E         - c
E         + 쫾

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py::test_valid_input[1a3f-0-2-2-1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py::test_valid_input[1A3F-0-2-2-1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py::test_valid_input[deadbeef-0-4-4-d]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_3_test_valid_input.py::test_valid_input[cafebabe-0-4-4-c]
============================== 4 failed in 0.14s ===============================
"""