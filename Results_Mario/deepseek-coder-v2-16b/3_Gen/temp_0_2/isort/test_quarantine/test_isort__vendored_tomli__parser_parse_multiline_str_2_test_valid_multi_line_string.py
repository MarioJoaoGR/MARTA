
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, skip_until
from isort._vendored.tomli._parser import ILLEGAL_MULTILINE_LITERAL_STR_CHARS

def test_valid_multi_line_string():
    src = 'Hello \\"""world\\"""'
    pos = 0
    new_pos, parsed_str = parse_multiline_str(src, pos, literal=True)
    assert parsed_str == "Hello \"\"\"world\"\"\""

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_valid_multi_line_string.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_multi_line_string _________________________

src = 'Hello \\"""world\\"""', pos = 3, expect = "'''"

    def skip_until(
        src: str,
        pos: Pos,
        expect: str,
        *,
        error_on: FrozenSet[str],
        error_on_eof: bool,
    ) -> Pos:
        try:
>           new_pos = src.index(expect, pos)
E           ValueError: substring not found

isort/isort/_vendored/tomli/_parser.py:250: ValueError

During handling of the above exception, another exception occurred:

    def test_valid_multi_line_string():
        src = 'Hello \\"""world\\"""'
        pos = 0
>       new_pos, parsed_str = parse_multiline_str(src, pos, literal=True)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_valid_multi_line_string.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:512: in parse_multiline_str
    end_pos = skip_until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'Hello \\"""world\\"""', pos = 3, expect = "'''"

    def skip_until(
        src: str,
        pos: Pos,
        expect: str,
        *,
        error_on: FrozenSet[str],
        error_on_eof: bool,
    ) -> Pos:
        try:
            new_pos = src.index(expect, pos)
        except ValueError:
            new_pos = len(src)
            if error_on_eof:
>               raise suffixed_err(src, new_pos, f'Expected "{expect!r}"')
E               isort._vendored.tomli._parser.TOMLDecodeError: Expected ""'''"" (at end of document)

isort/isort/_vendored/tomli/_parser.py:254: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_valid_multi_line_string.py::test_valid_multi_line_string
============================== 1 failed in 0.15s ===============================
"""