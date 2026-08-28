
import pytest
from isort.exceptions import MissingSection


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_MissingSection___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(MissingSection) as exc_info:
            raise MissingSection("requests", "thirdparty")
>       assert str(exc_info.value) == (
            f"Found requests import while parsing, but thirdparty was not included in the `sections` setting of your config. Please add it before continuing."
        )
E       AssertionError: assert 'Found reques...or more info.' == 'Found reques...e continuing.'
E         
E         Skipping 132 identical leading characters in diff, use -v to show
E         - continuing.
E         ?           ^
E         + continuing
E         ?           ^
E         + See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_MissingSection___init___0.py:8: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(MissingSection) as exc_info:
            raise MissingSection(None, None)
>       assert str(exc_info.value) == (
            f"Found None import while parsing, but None was not included in the `sections` setting of your config. Please add it before continuing."
        )
E       AssertionError: assert 'Found None i...or more info.' == 'Found None i...e continuing.'
E         
E         Skipping 122 identical leading characters in diff, use -v to show
E         - continuing.
E         ?           ^
E         + continuing
E         ?           ^
E         + See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_MissingSection___init___0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_MissingSection___init___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_MissingSection___init___0.py::test_edge_case_none
============================== 2 failed in 0.08s ===============================
"""