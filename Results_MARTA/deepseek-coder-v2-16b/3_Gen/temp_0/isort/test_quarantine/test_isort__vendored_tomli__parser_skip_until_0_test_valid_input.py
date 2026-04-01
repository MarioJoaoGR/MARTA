
import pytest
from isort._vendored.tomli._parser import skip_until, suffixed_err
from typing import FrozenSet

def test_valid_input():
    src = 'Hello, world!'
    pos = 0
    expect = 'world'
    error_on = frozenset({' ', '\n'})
    error_on_eof = False
    
    with pytest.raises(suffixed_err) as excinfo:
        new_pos = skip_until(src, pos, expect, error_on=error_on, error_on_eof=error_on_eof)
    
    assert 'Expected "world"' in str(excinfo.value)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        src = 'Hello, world!'
        pos = 0
        expect = 'world'
        error_on = frozenset({' ', '\n'})
        error_on_eof = False
    
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_valid_input.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.13s ===============================
"""