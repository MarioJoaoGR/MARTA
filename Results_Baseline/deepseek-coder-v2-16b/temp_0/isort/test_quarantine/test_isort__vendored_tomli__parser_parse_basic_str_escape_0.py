
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import parse_basic_str_escape, Pos

# Define the TOML whitespace characters for use in tests
TOML_WS = " \t"
TOML_WS_AND_NEWLINE = " \t\n"
BASIC_STR_ESCAPE_REPLACEMENTS = {
    "\\": "\\",
    "\"": "\"",
    "\b": "\b",
    "\f": "\f",
    "\n": "\n",
    "\r": "\r",
    "\t": "\t"
}

def skip_chars(src: str, pos: int, chars: str) -> int:
    while pos < len(src) and src[pos] in chars:
        pos += 1
    return pos

def suffixed_err(src: str, pos: int, msg: str) -> Exception:
    raise KeyError(msg)

# Test cases for parse_basic_str_escape function
@pytest.mark.parametrize("test_input, expected", [
    ("Hello\\nWorld", (Pos(12), "Hello\nWorld")),
    ("Hello\\tWorld", (Pos(12), "Hello\tWorld")),
    ("Hello\\\\World", (Pos(13), "Hello\\World")),
    ("Hello\\\"World", (Pos(13), 'Hello"World')),
])
def test_parse_basic_str_escape(test_input, expected):
    pos = Pos(0)
    result = parse_basic_str_escape(test_input, pos)
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________ test_parse_basic_str_escape[Hello\\nWorld-expected0] _____________

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

test_input = 'Hello\\nWorld', expected = (12, 'Hello\nWorld')

    @pytest.mark.parametrize("test_input, expected", [
        ("Hello\\nWorld", (Pos(12), "Hello\nWorld")),
        ("Hello\\tWorld", (Pos(12), "Hello\tWorld")),
        ("Hello\\\\World", (Pos(13), "Hello\\World")),
        ("Hello\\\"World", (Pos(13), 'Hello"World')),
    ])
    def test_parse_basic_str_escape(test_input, expected):
        pos = Pos(0)
>       result = parse_basic_str_escape(test_input, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py:36: 
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
_____________ test_parse_basic_str_escape[Hello\\tWorld-expected1] _____________

src = 'Hello\\tWorld', pos = 2

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

test_input = 'Hello\\tWorld', expected = (12, 'Hello\tWorld')

    @pytest.mark.parametrize("test_input, expected", [
        ("Hello\\nWorld", (Pos(12), "Hello\nWorld")),
        ("Hello\\tWorld", (Pos(12), "Hello\tWorld")),
        ("Hello\\\\World", (Pos(13), "Hello\\World")),
        ("Hello\\\"World", (Pos(13), 'Hello"World')),
    ])
    def test_parse_basic_str_escape(test_input, expected):
        pos = Pos(0)
>       result = parse_basic_str_escape(test_input, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Hello\\tWorld', pos = 2

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
____________ test_parse_basic_str_escape[Hello\\\\World-expected2] _____________

src = 'Hello\\\\World', pos = 2

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

test_input = 'Hello\\\\World', expected = (13, 'Hello\\World')

    @pytest.mark.parametrize("test_input, expected", [
        ("Hello\\nWorld", (Pos(12), "Hello\nWorld")),
        ("Hello\\tWorld", (Pos(12), "Hello\tWorld")),
        ("Hello\\\\World", (Pos(13), "Hello\\World")),
        ("Hello\\\"World", (Pos(13), 'Hello"World')),
    ])
    def test_parse_basic_str_escape(test_input, expected):
        pos = Pos(0)
>       result = parse_basic_str_escape(test_input, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Hello\\\\World', pos = 2

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
_____________ test_parse_basic_str_escape[Hello\\"World-expected3] _____________

src = 'Hello\\"World', pos = 2

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

test_input = 'Hello\\"World', expected = (13, 'Hello"World')

    @pytest.mark.parametrize("test_input, expected", [
        ("Hello\\nWorld", (Pos(12), "Hello\nWorld")),
        ("Hello\\tWorld", (Pos(12), "Hello\tWorld")),
        ("Hello\\\\World", (Pos(13), "Hello\\World")),
        ("Hello\\\"World", (Pos(13), 'Hello"World')),
    ])
    def test_parse_basic_str_escape(test_input, expected):
        pos = Pos(0)
>       result = parse_basic_str_escape(test_input, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Hello\\"World', pos = 2

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
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py::test_parse_basic_str_escape[Hello\\nWorld-expected0]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py::test_parse_basic_str_escape[Hello\\tWorld-expected1]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py::test_parse_basic_str_escape[Hello\\\\World-expected2]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0.py::test_parse_basic_str_escape[Hello\\"World-expected3]
============================== 4 failed in 0.16s ===============================
"""