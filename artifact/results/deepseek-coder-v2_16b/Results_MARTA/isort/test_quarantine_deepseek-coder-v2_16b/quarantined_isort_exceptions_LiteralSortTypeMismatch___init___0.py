
import pytest
from isort.exceptions import LiteralSortTypeMismatch


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralSortTypeMismatch___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        instance = LiteralSortTypeMismatch(kind=None, expected_kind=list)
        with pytest.raises(LiteralSortTypeMismatch) as excinfo:
            raise instance
>       assert str(excinfo.value) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'NoneType'>."
E       assert 'isort was to...of type None.' == "isort was to... 'NoneType'>."
E         
E         Skipping 78 identical leading characters in diff, use -v to show
E         - l of type <class 'NoneType'>.
E         + l of type None.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralSortTypeMismatch___init___0.py:9: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        instance = LiteralSortTypeMismatch(kind='incorrect_type', expected_kind=list)
        with pytest.raises(LiteralSortTypeMismatch) as excinfo:
            raise instance
>       assert str(excinfo.value) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'str'>."
E       assert 'isort was to...correct_type.' == "isort was to...class 'str'>."
E         
E         Skipping 78 identical leading characters in diff, use -v to show
E         - l of type <class 'str'>.
E         + l of type incorrect_type.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralSortTypeMismatch___init___0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralSortTypeMismatch___init___0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_LiteralSortTypeMismatch___init___0.py::test_invalid_input
============================== 2 failed in 0.08s ===============================
"""