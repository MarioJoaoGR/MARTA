
import pytest
from isort._vendored.tomli._parser import skip_until

def test_error_handling():
    src = "This is a test string with spaces and newlines."
    pos = 0
    expect = "spaces"
    error_on = frozenset({' ', '\n'})
    error_on_eof = True
    
    with pytest.raises(ValueError) as excinfo:
        skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)
    
    assert str(excinfo.value) == f'Expected "{expect!r}"'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        src = "This is a test string with spaces and newlines."
        pos = 0
        expect = "spaces"
        error_on = frozenset({' ', '\n'})
        error_on_eof = True
    
        with pytest.raises(ValueError) as excinfo:
            skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)
    
>       assert str(excinfo.value) == f'Expected "{expect!r}"'
E       assert 'Found invali... 1, column 5)' == 'Expected "\'spaces\'"'
E         
E         - Expected "'spaces'"
E         + Found invalid character "' '" (at line 1, column 5)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_error_handling.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_error_handling.py::test_error_handling
============================== 1 failed in 0.11s ===============================
"""