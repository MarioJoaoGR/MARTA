
import pytest
from isort.exceptions import LiteralParsingFailure

def test_valid_input():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure("pass", ValueError("Test error"))
    
    # The expected error message includes the exact string representation of the passed exception
    expected_error_message = (
        "isort failed to parse the given literal pass. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of ValueError('Test error')."
    )
    
    # Assert that the string representation of the raised exception matches the expected message
    assert str(exc_info.value) == expected_error_message

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

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(LiteralParsingFailure) as exc_info:
            raise LiteralParsingFailure("pass", ValueError("Test error"))
    
        # The expected error message includes the exact string representation of the passed exception
        expected_error_message = (
            "isort failed to parse the given literal pass. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of ValueError('Test error')."
        )
    
        # Assert that the string representation of the raised exception matches the expected message
>       assert str(exc_info.value) == expected_error_message
E       assert 'isort failed...f Test error.' == "isort failed...Test error')."
E         
E         Skipping 173 identical leading characters in diff, use -v to show
E         - eption of ValueError('Test error').
E         ?           ------------          --
E         + eption of Test error.

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""