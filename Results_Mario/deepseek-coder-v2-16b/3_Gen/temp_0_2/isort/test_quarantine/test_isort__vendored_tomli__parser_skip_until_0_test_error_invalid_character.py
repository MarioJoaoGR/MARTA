
import pytest
from isort._vendored.tomli._parser import skip_until, TOMLDecodeError

def test_error_invalid_character():
    src = "aabbcc"
    pos = 0
    expect = "cc"
    error_on = {"b", "c"}
    
    with pytest.raises(TOMLDecodeError) as excinfo:
        skip_until(src, pos, expect, error_on=error_on, error_on_eof=False)
    
    assert str(excinfo.value) == 'Found invalid character "b"'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_error_invalid_character.py F [100%]

=================================== FAILURES ===================================
_________________________ test_error_invalid_character _________________________

    def test_error_invalid_character():
        src = "aabbcc"
        pos = 0
        expect = "cc"
        error_on = {"b", "c"}
    
        with pytest.raises(TOMLDecodeError) as excinfo:
            skip_until(src, pos, expect, error_on=error_on, error_on_eof=False)
    
>       assert str(excinfo.value) == 'Found invalid character "b"'
E       assert 'Found invali... 1, column 3)' == 'Found invalid character "b"'
E         
E         - Found invalid character "b"
E         + Found invalid character "'b'" (at line 1, column 3)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_error_invalid_character.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_error_invalid_character.py::test_error_invalid_character
============================== 1 failed in 0.13s ===============================
"""