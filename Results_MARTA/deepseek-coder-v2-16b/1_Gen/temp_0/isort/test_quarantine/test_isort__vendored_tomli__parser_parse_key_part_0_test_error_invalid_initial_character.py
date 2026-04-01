
import pytest
from isort._vendored.tomli._parser import parse_key_part

def test_error_invalid_initial_character():
    with pytest.raises(ValueError) as excinfo:
        src = "!example"
        pos = 0
        parse_key_part(src, pos)
    assert str(excinfo.value) == 'Invalid initial character for a key part'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_error_invalid_initial_character.py F [100%]

=================================== FAILURES ===================================
_____________________ test_error_invalid_initial_character _____________________

    def test_error_invalid_initial_character():
        with pytest.raises(ValueError) as excinfo:
            src = "!example"
            pos = 0
            parse_key_part(src, pos)
>       assert str(excinfo.value) == 'Invalid initial character for a key part'
E       AssertionError: assert 'Invalid init... 1, column 1)' == 'Invalid init...or a key part'
E         
E         - Invalid initial character for a key part
E         + Invalid initial character for a key part (at line 1, column 1)
E         ?                                         ++++++++++++++++++++++

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_error_invalid_initial_character.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_error_invalid_initial_character.py::test_error_invalid_initial_character
============================== 1 failed in 0.11s ===============================
"""