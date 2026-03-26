
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, suffixed_err
from typing import Tuple

def test_valid_single_line():
    src = 'Hello\\nWorld'
    pos = 0
    new_pos, parsed_str = parse_basic_str_escape(src, pos)
    assert parsed_str == "Hello\nWorld"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_single_line.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_single_line ____________________________

src = 'Hello\\nWorld', pos = 2

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
E           KeyError: 'He'

isort/isort/_vendored/tomli/_parser.py:476: KeyError

During handling of the above exception, another exception occurred:

    def test_valid_single_line():
        src = 'Hello\\nWorld'
        pos = 0
>       new_pos, parsed_str = parse_basic_str_escape(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_single_line.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Hello\\nWorld', pos = 2

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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_single_line.py::test_valid_single_line
============================== 1 failed in 0.12s ===============================
"""