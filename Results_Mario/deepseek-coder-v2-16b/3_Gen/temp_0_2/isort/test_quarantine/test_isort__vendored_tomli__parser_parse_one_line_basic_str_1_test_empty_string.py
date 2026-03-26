
from isort._vendored.tomli._parser import parse_one_line_basic_str, parse_basic_str
import pytest

def test_empty_string():
    src = ''
    pos = 0
    with pytest.raises(IndexError):
        new_pos, parsed_str = parse_one_line_basic_str(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_1_test_empty_string.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_string _______________________________

src = '', pos = 1

    def parse_basic_str(src: str, pos: Pos, *, multiline: bool) -> Tuple[Pos, str]:
        if multiline:
            error_on = ILLEGAL_MULTILINE_BASIC_STR_CHARS
            parse_escapes = parse_basic_str_escape_multiline
        else:
            error_on = ILLEGAL_BASIC_STR_CHARS
            parse_escapes = parse_basic_str_escape
        result = ""
        start_pos = pos
        while True:
            try:
>               char = src[pos]
E               IndexError: string index out of range

isort/isort/_vendored/tomli/_parser.py:547: IndexError

During handling of the above exception, another exception occurred:

    def test_empty_string():
        src = ''
        pos = 0
        with pytest.raises(IndexError):
>           new_pos, parsed_str = parse_one_line_basic_str(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_1_test_empty_string.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:393: in parse_one_line_basic_str
    return parse_basic_str(src, pos, multiline=False)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '', pos = 1

    def parse_basic_str(src: str, pos: Pos, *, multiline: bool) -> Tuple[Pos, str]:
        if multiline:
            error_on = ILLEGAL_MULTILINE_BASIC_STR_CHARS
            parse_escapes = parse_basic_str_escape_multiline
        else:
            error_on = ILLEGAL_BASIC_STR_CHARS
            parse_escapes = parse_basic_str_escape
        result = ""
        start_pos = pos
        while True:
            try:
                char = src[pos]
            except IndexError:
>               raise suffixed_err(src, pos, "Unterminated string")
E               isort._vendored.tomli._parser.TOMLDecodeError: Unterminated string (at end of document)

isort/isort/_vendored/tomli/_parser.py:549: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_1_test_empty_string.py::test_empty_string
============================== 1 failed in 0.12s ===============================
"""