
import pytest
from isort.exceptions import LiteralParsingFailure

def test_invalid_input():
    with pytest.raises(TypeError):
        try:
            raise LiteralParsingFailure("some_literal", "not an exception")
        except LiteralParsingFailure as e:
            assert isinstance(e.original_error, Exception)

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

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            try:
>               raise LiteralParsingFailure("some_literal", "not an exception")
E               isort.exceptions.LiteralParsingFailure: isort failed to parse the given literal some_literal. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of not an exception.

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___2_test_invalid_input.py:8: LiteralParsingFailure

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        with pytest.raises(TypeError):
            try:
                raise LiteralParsingFailure("some_literal", "not an exception")
            except LiteralParsingFailure as e:
>               assert isinstance(e.original_error, Exception)
E               assert False
E                +  where False = isinstance('not an exception', Exception)
E                +    where 'not an exception' = LiteralParsingFailure("isort failed to parse the given literal some_literal. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of not an exception.").original_error

isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___2_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralParsingFailure___init___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""