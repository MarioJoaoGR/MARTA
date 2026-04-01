
import pytest
from isort.exceptions import LiteralParsingFailure

def test_invalid_input():
    with pytest.raises(LiteralParsingFailure) as exc_info:
        code = "class InvalidStructure: pass"
        raise LiteralParsingFailure(code, ValueError("Unsupported data structure"))
    
    assert str(exc_info.value) == (
        f"isort failed to parse the given literal {code}. It's important to note that isort literal sorting only supports "
        "simple literals parsable by ast.literal_eval which gave the exception of ValueError('Unsupported data structure')."
    )

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
        with pytest.raises(LiteralParsingFailure) as exc_info:
            code = "class InvalidStructure: pass"
            raise LiteralParsingFailure(code, ValueError("Unsupported data structure"))
    
>       assert str(exc_info.value) == (
            f"isort failed to parse the given literal {code}. It's important to note that isort literal sorting only supports "
            "simple literals parsable by ast.literal_eval which gave the exception of ValueError('Unsupported data structure')."
        )
E       assert 'isort failed...ta structure.' == "isort failed... structure')."
E         
E         Skipping 197 identical leading characters in diff, use -v to show
E         - eption of ValueError('Unsupported data structure').
E         ?           ------------                          --
E         + eption of Unsupported data structure.

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""