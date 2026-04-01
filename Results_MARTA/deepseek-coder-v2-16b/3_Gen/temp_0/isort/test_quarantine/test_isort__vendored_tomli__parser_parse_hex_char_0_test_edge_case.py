
from isort._vendored.tomli._parser import parse_hex_char
import pytest

HEXDIGIT_CHARS = set("0123456789ABCDEFabcdef")

def is_unicode_scalar_value(n: int) -> bool:
    return 0 <= n <= 0x10FFFF and (n < 0xD800 or n > 0xDFFF) and (n < 0xE000 or n > 0xF8FF)

def suffixed_err(src: str, pos: int, msg: str) -> ValueError:
    raise ValueError(f"Error at position {pos}: {msg}")

@pytest.mark.parametrize("src, pos, hex_len, expected", [
    ("48656c6c6f20776f726c64", 0, 2, (2, 'H')),
    ("48656c6c6f20776f726c64", 7, 2, (9, 'o')),
    ("48656c6c6f20776f726c64", 16, 2, (18, 'd')),
])
def test_parse_hex_char(src: str, pos: int, hex_len: int, expected: tuple[int, str]):
    result = parse_hex_char(src, pos, hex_len)
    assert result == expected

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_test_edge_case.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________ test_parse_hex_char[48656c6c6f20776f726c64-7-2-expected1] ___________

src = '48656c6c6f20776f726c64', pos = 7, hex_len = 2, expected = (9, 'o')

    @pytest.mark.parametrize("src, pos, hex_len, expected", [
        ("48656c6c6f20776f726c64", 0, 2, (2, 'H')),
        ("48656c6c6f20776f726c64", 7, 2, (9, 'o')),
        ("48656c6c6f20776f726c64", 16, 2, (18, 'd')),
    ])
    def test_parse_hex_char(src: str, pos: int, hex_len: int, expected: tuple[int, str]):
        result = parse_hex_char(src, pos, hex_len)
>       assert result == expected
E       AssertionError: assert (9, 'Æ') == (9, 'o')
E         
E         At index 1 diff: 'Æ' != 'o'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_test_edge_case.py:20: AssertionError
__________ test_parse_hex_char[48656c6c6f20776f726c64-16-2-expected2] __________

src = '48656c6c6f20776f726c64', pos = 16, hex_len = 2, expected = (18, 'd')

    @pytest.mark.parametrize("src, pos, hex_len, expected", [
        ("48656c6c6f20776f726c64", 0, 2, (2, 'H')),
        ("48656c6c6f20776f726c64", 7, 2, (9, 'o')),
        ("48656c6c6f20776f726c64", 16, 2, (18, 'd')),
    ])
    def test_parse_hex_char(src: str, pos: int, hex_len: int, expected: tuple[int, str]):
        result = parse_hex_char(src, pos, hex_len)
>       assert result == expected
E       AssertionError: assert (18, 'r') == (18, 'd')
E         
E         At index 1 diff: 'r' != 'd'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_test_edge_case.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_test_edge_case.py::test_parse_hex_char[48656c6c6f20776f726c64-7-2-expected1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_test_edge_case.py::test_parse_hex_char[48656c6c6f20776f726c64-16-2-expected2]
========================= 2 failed, 1 passed in 0.11s ==========================
"""