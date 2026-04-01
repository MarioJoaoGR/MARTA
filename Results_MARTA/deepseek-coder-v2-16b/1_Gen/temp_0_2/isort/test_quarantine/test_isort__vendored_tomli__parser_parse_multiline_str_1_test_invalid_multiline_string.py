
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, Pos

def test_invalid_multiline_string():
    with pytest.raises(ValueError) as excinfo:
        pos, parsed_str = parse_multiline_str('''this is a test''', Pos(0), literal=True)
    assert "Illegal character" in str(excinfo.value)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_1_test_invalid_multiline_string.py F [100%]

=================================== FAILURES ===================================
________________________ test_invalid_multiline_string _________________________

    def test_invalid_multiline_string():
        with pytest.raises(ValueError) as excinfo:
            pos, parsed_str = parse_multiline_str('''this is a test''', Pos(0), literal=True)
>       assert "Illegal character" in str(excinfo.value)
E       assert 'Illegal character' in 'Expected ""\'\'\'"" (at end of document)'
E        +  where 'Expected ""\'\'\'"" (at end of document)' = str(TOMLDecodeError('Expected ""\'\'\'"" (at end of document)'))
E        +    where TOMLDecodeError('Expected ""\'\'\'"" (at end of document)') = <ExceptionInfo TOMLDecodeError('Expected ""\'\'\'"" (at end of document)') tblen=3>.value

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_1_test_invalid_multiline_string.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_1_test_invalid_multiline_string.py::test_invalid_multiline_string
============================== 1 failed in 0.13s ===============================
"""