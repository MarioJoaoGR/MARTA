
import pytest
from isort.exceptions import LiteralParsingFailure


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_literal_parsing _________________________

    def test_invalid_literal_parsing():
        code = "[1, 2, 'three']"  # An invalid list literal
        with pytest.raises(LiteralParsingFailure) as exc_info:
            raise LiteralParsingFailure(code, ValueError("Invalid syntax"))
>       assert str(exc_info.value) == (
            f"isort failed to parse the given literal {code}. It's important to note that isort "
            "literal sorting only supports simple literals parsable by ast.literal_eval which gave "
            "the exception of ValueError('Invalid syntax')."
        )
E       assert 'isort failed...valid syntax.' == "isort failed...lid syntax')."
E         
E         Skipping 184 identical leading characters in diff, use -v to show
E         - eption of ValueError('Invalid syntax').
E         ?           ------------              --
E         + eption of Invalid syntax.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py:9: AssertionError
___________________________ test_missing_parameters ____________________________

    def test_missing_parameters():
        with pytest.raises(LiteralParsingFailure) as exc_info:
>           raise LiteralParsingFailure()
E           TypeError: LiteralParsingFailure.__init__() missing 2 required positional arguments: 'code' and 'original_error'

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py:17: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py::test_invalid_literal_parsing
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py::test_missing_parameters
============================== 2 failed in 0.08s ===============================
"""