
import pytest
from isort._vendored.tomli._parser import parse_hex_char, HEXDIGIT_CHARS

@pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
    ("48656c6c6f20776f726c6421", 0, 2, 2, "H"),
    ("48656c6c6f20776f726c6421", 7, 2, 9, "o"),
    ("48656c6c6f20776f726c6421", 14, 2, 16, "w"),
])
def test_parse_hex_char(src, pos, hex_len, expected_pos, expected_char):
    actual_pos, actual_char = parse_hex_char(src, pos, hex_len)
    assert actual_pos == expected_pos
    assert actual_char == expected_char

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_valid_input_happy_path.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________ test_parse_hex_char[48656c6c6f20776f726c6421-7-2-9-o] _____________

src = '48656c6c6f20776f726c6421', pos = 7, hex_len = 2, expected_pos = 9
expected_char = 'o'

    @pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
        ("48656c6c6f20776f726c6421", 0, 2, 2, "H"),
        ("48656c6c6f20776f726c6421", 7, 2, 9, "o"),
        ("48656c6c6f20776f726c6421", 14, 2, 16, "w"),
    ])
    def test_parse_hex_char(src, pos, hex_len, expected_pos, expected_char):
        actual_pos, actual_char = parse_hex_char(src, pos, hex_len)
        assert actual_pos == expected_pos
>       assert actual_char == expected_char
E       AssertionError: assert 'Æ' == 'o'
E         
E         - o
E         + Æ

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_valid_input_happy_path.py:13: AssertionError
___________ test_parse_hex_char[48656c6c6f20776f726c6421-14-2-16-w] ____________

src = '48656c6c6f20776f726c6421', pos = 14, hex_len = 2, expected_pos = 16
expected_char = 'w'

    @pytest.mark.parametrize("src, pos, hex_len, expected_pos, expected_char", [
        ("48656c6c6f20776f726c6421", 0, 2, 2, "H"),
        ("48656c6c6f20776f726c6421", 7, 2, 9, "o"),
        ("48656c6c6f20776f726c6421", 14, 2, 16, "w"),
    ])
    def test_parse_hex_char(src, pos, hex_len, expected_pos, expected_char):
        actual_pos, actual_char = parse_hex_char(src, pos, hex_len)
        assert actual_pos == expected_pos
>       assert actual_char == expected_char
E       AssertionError: assert 'o' == 'w'
E         
E         - w
E         + o

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_valid_input_happy_path.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_valid_input_happy_path.py::test_parse_hex_char[48656c6c6f20776f726c6421-7-2-9-o]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0_valid_input_happy_path.py::test_parse_hex_char[48656c6c6f20776f726c6421-14-2-16-w]
========================= 2 failed, 1 passed in 0.13s ==========================
"""