
import pytest
from isort._vendored.tomli._parser import skip_chars

# Test cases for skip_chars function
def test_skip_chars_basic():
    result = skip_chars("hello world", 0, ["l", "o"])
    assert result == 5

def test_skip_chars_specific_position():
    result = skip_chars("hello world", 3, ["l", "o"])
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_skip_chars_basic _____________________________

    def test_skip_chars_basic():
        result = skip_chars("hello world", 0, ["l", "o"])
>       assert result == 5
E       assert 0 == 5

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_0.py::test_skip_chars_basic
========================= 1 failed, 1 passed in 0.09s ==========================
"""