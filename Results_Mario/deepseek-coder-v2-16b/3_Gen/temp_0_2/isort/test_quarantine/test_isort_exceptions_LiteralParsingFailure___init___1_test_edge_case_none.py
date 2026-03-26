
import pytest
from isort.exceptions import LiteralParsingFailure

def test_edge_case_none():
    code = None
    original_error = None

    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)

    assert str(exc_info.value) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
    assert exc_info.value.code == code
    assert isinstance(exc_info.value.original_error, type) and exc_info.value.original_error is None

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

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        code = None
        original_error = None
    
        with pytest.raises(LiteralParsingFailure) as exc_info:
            raise LiteralParsingFailure(code, original_error)
    
        assert str(exc_info.value) == (
            f"isort failed to parse the given literal {code}. It's important to note "
            "that isort literal sorting only supports simple literals parsable by "
            f"ast.literal_eval which gave the exception of {original_error}."
        )
        assert exc_info.value.code == code
>       assert isinstance(exc_info.value.original_error, type) and exc_info.value.original_error is None
E       assert (False)
E        +  where False = isinstance(None, type)
E        +    where None = LiteralParsingFailure("isort failed to parse the given literal None. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of None.").original_error
E        +      where LiteralParsingFailure("isort failed to parse the given literal None. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of None.") = <ExceptionInfo LiteralParsingFailure("isort failed to parse the given literal None. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of None.") tblen=1>.value

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_edge_case_none.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.12s ===============================
"""