
import pytest
from isort._vendored.tomli._parser import skip_until, suffixed_err

def test_invalid_input():
    src = "abc def ghi"
    pos = 0
    expect = "def"
    error_on = frozenset({' '})
    error_on_eof = True
    
    try:
        result = skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)
        assert result == 4  # The position where "def" starts is at index 4.
    except ValueError as e:
        assert str(e) == f'Expected "{expect!r}"'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        src = "abc def ghi"
        pos = 0
        expect = "def"
        error_on = frozenset({' '})
        error_on_eof = True
    
        try:
>           result = skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_invalid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'abc def ghi', pos = 3, expect = 'def'

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
                raise suffixed_err(src, new_pos, f'Expected "{expect!r}"')
    
        if not error_on.isdisjoint(src[pos:new_pos]):
            while src[pos] not in error_on:
                pos += 1
>           raise suffixed_err(src, pos, f'Found invalid character "{src[pos]!r}"')
E           isort._vendored.tomli._parser.TOMLDecodeError: Found invalid character "' '" (at line 1, column 4)

isort/isort/_vendored/tomli/_parser.py:259: TOMLDecodeError

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        src = "abc def ghi"
        pos = 0
        expect = "def"
        error_on = frozenset({' '})
        error_on_eof = True
    
        try:
            result = skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)
            assert result == 4  # The position where "def" starts is at index 4.
        except ValueError as e:
>           assert str(e) == f'Expected "{expect!r}"'
E           assert 'Found invali... 1, column 4)' == 'Expected "\'def\'"'
E             
E             - Expected "'def'"
E             + Found invalid character "' '" (at line 1, column 4)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""