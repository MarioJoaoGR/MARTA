
import pytest
from isort._vendored.tomli._parser import (
    parse_basic_str_escape, Pos, TOML_WS, TOML_WS_AND_NEWLINE, BASIC_STR_ESCAPE_REPLACEMENTS, suffixed_err
)

@pytest.mark.parametrize("src, expected", [
    ("Line1\\nLine2", "Line1\nLine2"),
    ("Hello\\tWorld", "Hello\tWorld"),
    ("Escape \\\\ sequence", "Escape \\ sequence"),
    ('Multiline \\ \n string', 'Multiline  \n string'),
])
def test_valid_case_multi_line(src, expected):
    pos = Pos(0)
    _, result = parse_basic_str_escape(src, pos, multiline=True)
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
collected 4 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
____________ test_valid_case_multi_line[Line1\\nLine2-Line1\nLine2] ____________

src = 'Line1\\nLine2', pos = 2

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
E           KeyError: 'Li'

isort/isort/_vendored/tomli/_parser.py:476: KeyError

During handling of the above exception, another exception occurred:

src = 'Line1\\nLine2', expected = 'Line1\nLine2'

    @pytest.mark.parametrize("src, expected", [
        ("Line1\\nLine2", "Line1\nLine2"),
        ("Hello\\tWorld", "Hello\tWorld"),
        ("Escape \\\\ sequence", "Escape \\ sequence"),
        ('Multiline \\ \n string', 'Multiline  \n string'),
    ])
    def test_valid_case_multi_line(src, expected):
        pos = Pos(0)
>       _, result = parse_basic_str_escape(src, pos, multiline=True)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Line1\\nLine2', pos = 2

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
____________ test_valid_case_multi_line[Hello\\tWorld-Hello\tWorld] ____________

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

src = 'Hello\\tWorld', expected = 'Hello\tWorld'

    @pytest.mark.parametrize("src, expected", [
        ("Line1\\nLine2", "Line1\nLine2"),
        ("Hello\\tWorld", "Hello\tWorld"),
        ("Escape \\\\ sequence", "Escape \\ sequence"),
        ('Multiline \\ \n string', 'Multiline  \n string'),
    ])
    def test_valid_case_multi_line(src, expected):
        pos = Pos(0)
>       _, result = parse_basic_str_escape(src, pos, multiline=True)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py:15: 
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
_____ test_valid_case_multi_line[Escape \\\\ sequence-Escape \\ sequence] ______

src = 'Escape \\\\ sequence', pos = 2

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
E           KeyError: 'Es'

isort/isort/_vendored/tomli/_parser.py:476: KeyError

During handling of the above exception, another exception occurred:

src = 'Escape \\\\ sequence', expected = 'Escape \\ sequence'

    @pytest.mark.parametrize("src, expected", [
        ("Line1\\nLine2", "Line1\nLine2"),
        ("Hello\\tWorld", "Hello\tWorld"),
        ("Escape \\\\ sequence", "Escape \\ sequence"),
        ('Multiline \\ \n string', 'Multiline  \n string'),
    ])
    def test_valid_case_multi_line(src, expected):
        pos = Pos(0)
>       _, result = parse_basic_str_escape(src, pos, multiline=True)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Escape \\\\ sequence', pos = 2

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
___ test_valid_case_multi_line[Multiline \\ \n string-Multiline  \n string] ____

src = 'Multiline \\ \n string', pos = 2

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
E           KeyError: 'Mu'

isort/isort/_vendored/tomli/_parser.py:476: KeyError

During handling of the above exception, another exception occurred:

src = 'Multiline \\ \n string', expected = 'Multiline  \n string'

    @pytest.mark.parametrize("src, expected", [
        ("Line1\\nLine2", "Line1\nLine2"),
        ("Hello\\tWorld", "Hello\tWorld"),
        ("Escape \\\\ sequence", "Escape \\ sequence"),
        ('Multiline \\ \n string', 'Multiline  \n string'),
    ])
    def test_valid_case_multi_line(src, expected):
        pos = Pos(0)
>       _, result = parse_basic_str_escape(src, pos, multiline=True)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Multiline \\ \n string', pos = 2

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
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py::test_valid_case_multi_line[Line1\\nLine2-Line1\nLine2]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py::test_valid_case_multi_line[Hello\\tWorld-Hello\tWorld]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py::test_valid_case_multi_line[Escape \\\\ sequence-Escape \\ sequence]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py::test_valid_case_multi_line[Multiline \\ \n string-Multiline  \n string]
============================== 4 failed in 0.18s ===============================
"""