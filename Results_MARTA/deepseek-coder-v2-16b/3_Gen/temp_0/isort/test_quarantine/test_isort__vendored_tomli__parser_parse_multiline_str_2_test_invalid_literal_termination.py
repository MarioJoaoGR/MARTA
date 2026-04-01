
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, Pos

def test_invalid_literal_termination():
    with pytest.raises(ValueError) as excinfo:
        src = '"""Hello\nWorld'
        pos = Pos(0)
        literal = True
        parse_multiline_str(src, pos, literal=literal)
    
    assert str(excinfo.value) == "tomli._parser:123: unterminated string (at least one '\"\"\"')"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_invalid_literal_termination.py F [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_literal_termination _______________________

    def test_invalid_literal_termination():
        with pytest.raises(ValueError) as excinfo:
            src = '"""Hello\nWorld'
            pos = Pos(0)
            literal = True
            parse_multiline_str(src, pos, literal=literal)
    
>       assert str(excinfo.value) == "tomli._parser:123: unterminated string (at least one '\"\"\"')"
E       assert 'Expected ""\... of document)' == 'tomli._parse... one \'"""\')'
E         
E         - tomli._parser:123: unterminated string (at least one '"""')
E         + Expected ""'''"" (at end of document)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_invalid_literal_termination.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_invalid_literal_termination.py::test_invalid_literal_termination
============================== 1 failed in 0.11s ===============================
"""