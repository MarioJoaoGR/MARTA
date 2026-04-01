
import pytest
from isort.exceptions import LiteralParsingFailure

def test_invalid_input():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        code = "invalid syntax"
        raise LiteralParsingFailure(code, SyntaxError("Invalid syntax"))

    expected_error_message = (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of SyntaxError('Invalid syntax')."
    )

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

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(LiteralParsingFailure) as exc_info:
            code = "invalid syntax"
            raise LiteralParsingFailure(code, SyntaxError("Invalid syntax"))
    
        expected_error_message = (
            f"isort failed to parse the given literal {code}. It's important to note "
            "that isort literal sorting only supports simple literals parsable by "
            f"ast.literal_eval which gave the exception of SyntaxError('Invalid syntax')."
        )
    
>       assert str(exc_info.value) == expected_error_message
E       assert 'isort failed...valid syntax.' == "isort failed...lid syntax')."
E         
E         Skipping 183 identical leading characters in diff, use -v to show
E         - eption of SyntaxError('Invalid syntax').
E         ?           -------------              --
E         + eption of Invalid syntax.

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___0_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""