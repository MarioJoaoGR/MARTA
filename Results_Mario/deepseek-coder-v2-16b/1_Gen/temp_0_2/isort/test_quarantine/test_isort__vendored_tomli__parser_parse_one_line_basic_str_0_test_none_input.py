
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import Pos, parse_one_line_basic_str

def test_none_input():
    with pytest.raises(ValueError):
        pos, parsed_str = parse_one_line_basic_str(None, Pos(0))

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(ValueError):
>           pos, parsed_str = parse_one_line_basic_str(None, Pos(0))

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:393: in parse_one_line_basic_str
    return parse_basic_str(src, pos, multiline=False)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = None, pos = 1

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
E               TypeError: 'NoneType' object is not subscriptable

isort/isort/_vendored/tomli/_parser.py:547: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_none_input.py::test_none_input
============================== 1 failed in 0.12s ===============================
"""