
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, Pos

@pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
    ("\\u1234", 0, False, IndexError),
    ("\\U12345678", 0, False, IndexError),
    ("\\u123", 0, False, ValueError),
    ("\\U1234567", 0, False, ValueError),
    ("\\x1234", 0, False, KeyError),
    ("\\ ", 0, True, IndexError),
    ("\\\t", 0, True, IndexError),
    ("\\\n", 0, True, IndexError),
    ("\\ \n", 0, True, ValueError),
])
def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
    with pytest.raises(expected_error):
        parse_basic_str_escape(input_str, Pos(pos), multiline=multiline)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 9 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py F [ 11%]
F..FFFFF                                                                 [100%]

=================================== FAILURES ===================================
________ test_invalid_input_error_handling[\\u1234-0-False-IndexError] _________

input_str = '\\u1234', pos = 0, multiline = False
expected_error = <class 'IndexError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
>       with pytest.raises(expected_error):
E       Failed: DID NOT RAISE <class 'IndexError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:17: Failed
______ test_invalid_input_error_handling[\\U12345678-0-False-IndexError] _______

input_str = '\\U12345678', pos = 0, multiline = False
expected_error = <class 'IndexError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
        with pytest.raises(expected_error):
>           parse_basic_str_escape(input_str, Pos(pos), multiline=multiline)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:474: in parse_basic_str_escape
    return parse_hex_char(src, pos, 8)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '\\U12345678', pos = 10, hex_len = 8

    def parse_hex_char(src: str, pos: Pos, hex_len: int) -> Tuple[Pos, str]:
        hex_str = src[pos : pos + hex_len]
        if len(hex_str) != hex_len or not HEXDIGIT_CHARS.issuperset(hex_str):
            raise suffixed_err(src, pos, "Invalid hex value")
        pos += hex_len
        hex_int = int(hex_str, 16)
        if not is_unicode_scalar_value(hex_int):
>           raise suffixed_err(src, pos, "Escaped character is not a Unicode scalar value")
E           isort._vendored.tomli._parser.TOMLDecodeError: Escaped character is not a Unicode scalar value (at end of document)

isort/isort/_vendored/tomli/_parser.py:494: TOMLDecodeError
_________ test_invalid_input_error_handling[\\x1234-0-False-KeyError] __________

src = '\\x1234', pos = 2

    def parse_basic_str_escape(  # noqa: C901
        src: str, pos: Pos, *, multiline: bool = False
    ) -> Tuple[Pos, str]:
        escape_id = src[pos : pos + 2]
        pos += 2
        if multiline and escape_id in {"\\ ", "\\\t", "\\\n"}:
            # Skip whitespace until next non-whitespace character or end of
            # the doc. Error if non-whitespace is found before newline.
            if escape_id != "\\\n":
                pos = skip_chars(src, pos, TOML_WS)
                try:
                    char = src[pos]
                except IndexError:
                    return pos, ""
                if char != "\n":
                    raise suffixed_err(src, pos, 'Unescaped "\\" in a string')
                pos += 1
            pos = skip_chars(src, pos, TOML_WS_AND_NEWLINE)
            return pos, ""
        if escape_id == "\\u":
            return parse_hex_char(src, pos, 4)
        if escape_id == "\\U":
            return parse_hex_char(src, pos, 8)
        try:
>           return pos, BASIC_STR_ESCAPE_REPLACEMENTS[escape_id]
E           KeyError: '\\x'

isort/isort/_vendored/tomli/_parser.py:476: KeyError

During handling of the above exception, another exception occurred:

input_str = '\\x1234', pos = 0, multiline = False
expected_error = <class 'KeyError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
        with pytest.raises(expected_error):
>           parse_basic_str_escape(input_str, Pos(pos), multiline=multiline)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '\\x1234', pos = 2

    def parse_basic_str_escape(  # noqa: C901
        src: str, pos: Pos, *, multiline: bool = False
    ) -> Tuple[Pos, str]:
        escape_id = src[pos : pos + 2]
        pos += 2
        if multiline and escape_id in {"\\ ", "\\\t", "\\\n"}:
            # Skip whitespace until next non-whitespace character or end of
            # the doc. Error if non-whitespace is found before newline.
            if escape_id != "\\\n":
                pos = skip_chars(src, pos, TOML_WS)
                try:
                    char = src[pos]
                except IndexError:
                    return pos, ""
                if char != "\n":
                    raise suffixed_err(src, pos, 'Unescaped "\\" in a string')
                pos += 1
            pos = skip_chars(src, pos, TOML_WS_AND_NEWLINE)
            return pos, ""
        if escape_id == "\\u":
            return parse_hex_char(src, pos, 4)
        if escape_id == "\\U":
            return parse_hex_char(src, pos, 8)
        try:
            return pos, BASIC_STR_ESCAPE_REPLACEMENTS[escape_id]
        except KeyError:
            if len(escape_id) != 2:
                raise suffixed_err(src, pos, "Unterminated string")
>           raise suffixed_err(src, pos, 'Unescaped "\\" in a string')
E           isort._vendored.tomli._parser.TOMLDecodeError: Unescaped "\" in a string (at line 1, column 3)

isort/isort/_vendored/tomli/_parser.py:480: TOMLDecodeError
___________ test_invalid_input_error_handling[\\ -0-True-IndexError] ___________

input_str = '\\ ', pos = 0, multiline = True
expected_error = <class 'IndexError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
>       with pytest.raises(expected_error):
E       Failed: DID NOT RAISE <class 'IndexError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:17: Failed
__________ test_invalid_input_error_handling[\\\t-0-True-IndexError] ___________

input_str = '\\\t', pos = 0, multiline = True
expected_error = <class 'IndexError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
>       with pytest.raises(expected_error):
E       Failed: DID NOT RAISE <class 'IndexError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:17: Failed
__________ test_invalid_input_error_handling[\\\n-0-True-IndexError] ___________

input_str = '\\\n', pos = 0, multiline = True
expected_error = <class 'IndexError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
>       with pytest.raises(expected_error):
E       Failed: DID NOT RAISE <class 'IndexError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:17: Failed
__________ test_invalid_input_error_handling[\\ \n-0-True-ValueError] __________

input_str = '\\ \n', pos = 0, multiline = True
expected_error = <class 'ValueError'>

    @pytest.mark.parametrize("input_str, pos, multiline, expected_error", [
        ("\\u1234", 0, False, IndexError),
        ("\\U12345678", 0, False, IndexError),
        ("\\u123", 0, False, ValueError),
        ("\\U1234567", 0, False, ValueError),
        ("\\x1234", 0, False, KeyError),
        ("\\ ", 0, True, IndexError),
        ("\\\t", 0, True, IndexError),
        ("\\\n", 0, True, IndexError),
        ("\\ \n", 0, True, ValueError),
    ])
    def test_invalid_input_error_handling(input_str, pos, multiline, expected_error):
>       with pytest.raises(expected_error):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\u1234-0-False-IndexError]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\U12345678-0-False-IndexError]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\x1234-0-False-KeyError]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\ -0-True-IndexError]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\\t-0-True-IndexError]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\\n-0-True-IndexError]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling[\\ \n-0-True-ValueError]
========================= 7 failed, 2 passed in 0.17s ==========================
"""