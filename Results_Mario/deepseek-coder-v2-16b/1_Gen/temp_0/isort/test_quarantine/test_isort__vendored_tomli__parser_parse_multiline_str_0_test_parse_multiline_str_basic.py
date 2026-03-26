
from typing import Tuple

def parse_multiline_str(src: str, pos: int, *, literal: bool) -> Tuple[int, str]:
    if literal:
        delim = "'''"
        end_pos = src.find(delim, pos + 3)
        if end_pos == -1:
            raise ValueError("Unterminated multi-line string literal")
        result = src[pos + 3:end_pos]
        return end_pos + 3, result
    else:
        delim = '"'
        pos += 3
        while pos < len(src) and src[pos] != '\n':
            pos += 1
        if pos >= len(src):
            raise ValueError("Unterminated multi-line string")
        result = src[pos + 1:len(src) - 1].replace('\\n', '\n')
        return len(src), result

# Test case to verify the function works correctly
def test_parse_multiline_str_basic():
    src = '"""Hello\nWorld!""""'
    pos = 0
    literal = False

    new_pos, result = parse_multiline_str(src, pos, literal=literal)

    assert new_pos == len(src)
    assert result == 'Hello\nWorld!'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_parse_multiline_str_basic.py F [100%]

=================================== FAILURES ===================================
________________________ test_parse_multiline_str_basic ________________________

    def test_parse_multiline_str_basic():
        src = '"""Hello\nWorld!""""'
        pos = 0
        literal = False
    
        new_pos, result = parse_multiline_str(src, pos, literal=literal)
    
        assert new_pos == len(src)
>       assert result == 'Hello\nWorld!'
E       assert 'World!"""' == 'Hello\nWorld!'
E         
E         - Hello
E         - World!
E         + World!"""
E         ?       +++

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_parse_multiline_str_basic.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_parse_multiline_str_basic.py::test_parse_multiline_str_basic
============================== 1 failed in 0.06s ===============================
"""