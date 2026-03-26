
import pytest
from isort._vendored.tomli._parser import parse_literal_str, skip_until, ILLEGAL_LITERAL_STR_CHARS

def test_valid_case_2():
    src = "hello there"
    pos = 0
    new_pos, lit_str = parse_literal_str(src, pos)
    assert new_pos == len(src), f"Expected position to be at the end of the string but got {new_pos}"
    assert lit_str == "hello there", f"Expected literal string to be 'hello there' but got '{lit_str}'"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_case_2.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_2 _______________________________

src = 'hello there', pos = 1, expect = "'"

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

    def test_valid_case_2():
        src = "hello there"
        pos = 0
>       new_pos, lit_str = parse_literal_str(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_case_2.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:501: in parse_literal_str
    pos = skip_until(src, pos, "'", error_on=ILLEGAL_LITERAL_STR_CHARS, error_on_eof=True)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'hello there', pos = 1, expect = "'"

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
E               isort._vendored.tomli._parser.TOMLDecodeError: Expected ""'"" (at end of document)

isort/isort/_vendored/tomli/_parser.py:254: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_case_2.py::test_valid_case_2
============================== 1 failed in 0.12s ===============================
"""