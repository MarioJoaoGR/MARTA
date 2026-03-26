
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, TOMLDecodeError

def test_valid_basic_string():
    src = 'Hello "world"'
    pos = 0
    with pytest.raises(TOMLDecodeError) as excinfo:
        new_pos, parsed_str = parse_multiline_str(src, pos, literal=False)
    assert str(excinfo.value) == "Unterminated string (at end of document)"

def test_valid_multiline_string():
    src = 'Hello \\"""world\\"""'
    pos = 0
    with pytest.raises(TOMLDecodeError) as excinfo:
        new_pos, parsed_str = parse_multiline_str(src, pos, literal=True)
    assert str(excinfo.value) == "Expected \"'''\""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_basic_string.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_multiline_string __________________________

    def test_valid_multiline_string():
        src = 'Hello \\"""world\\"""'
        pos = 0
        with pytest.raises(TOMLDecodeError) as excinfo:
            new_pos, parsed_str = parse_multiline_str(src, pos, literal=True)
>       assert str(excinfo.value) == "Expected \"'''\""
E       assert 'Expected ""\... of document)' == 'Expected "\'\'\'"'
E         
E         - Expected "'''"
E         + Expected ""'''"" (at end of document)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_basic_string.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_basic_string.py::test_valid_multiline_string
========================= 1 failed, 1 passed in 0.13s ==========================
"""