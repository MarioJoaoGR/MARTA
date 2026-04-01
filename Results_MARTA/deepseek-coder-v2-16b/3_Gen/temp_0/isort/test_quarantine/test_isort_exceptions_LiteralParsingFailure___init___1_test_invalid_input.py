
import pytest
from isort.exceptions import LiteralParsingFailure

def test_invalid_input():
    code = '[1, [2, 3], 4]'
    with pytest.raises(LiteralParsingFailure) as exc_info:
        # This will cause an error since lists are not parsable by ast.literal_eval
        parsed_literal = eval(code)
    assert isinstance(exc_info.value, LiteralParsingFailure), f"Expected LiteralParsingFailure but got {type(exc_info.value)}"

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

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        code = '[1, [2, 3], 4]'
>       with pytest.raises(LiteralParsingFailure) as exc_info:
E       Failed: DID NOT RAISE <class 'isort.exceptions.LiteralParsingFailure'>

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""