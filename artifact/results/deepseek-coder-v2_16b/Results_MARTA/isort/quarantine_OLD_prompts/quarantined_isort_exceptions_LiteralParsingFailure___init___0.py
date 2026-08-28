
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(LiteralParsingFailure) as excinfo:
            raise LiteralParsingFailure("valid_literal", ValueError("Parsing error"))
>       assert str(excinfo.value) == "isort failed to parse the given literal valid_literal. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of ValueError('Parsing error')."
E       assert 'isort failed...arsing error.' == "isort failed...sing error')."
E         
E         Skipping 182 identical leading characters in diff, use -v to show
E         - eption of ValueError('Parsing error').
E         ?           ------------             --
E         + eption of Parsing error.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py:8: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(LiteralParsingFailure) as excinfo:
            raise LiteralParsingFailure("literal_with_None", ValueError("Parsing error"))
>       assert str(excinfo.value) == "isort failed to parse the given literal literal_with_None. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of ValueError('Parsing error')."
E       assert 'isort failed...arsing error.' == "isort failed...sing error')."
E         
E         Skipping 186 identical leading characters in diff, use -v to show
E         - eption of ValueError('Parsing error').
E         ?           ------------             --
E         + eption of Parsing error.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py:13: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(LiteralParsingFailure) as excinfo:
            raise LiteralParsingFailure("invalid_literal", ValueError("Invalid parsing"))
>       assert str(excinfo.value) == "isort failed to parse the given literal invalid_literal. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of ValueError('Invalid parsing')."
E       assert 'isort failed...alid parsing.' == "isort failed...id parsing')."
E         
E         Skipping 184 identical leading characters in diff, use -v to show
E         - eption of ValueError('Invalid parsing').
E         ?           ------------               --
E         + eption of Invalid parsing.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralParsingFailure___init___0.py::test_invalid_input
============================== 3 failed in 0.09s ===============================
"""