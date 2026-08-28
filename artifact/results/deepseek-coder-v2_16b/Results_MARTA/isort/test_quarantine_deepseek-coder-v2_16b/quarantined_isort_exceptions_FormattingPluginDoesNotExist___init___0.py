
import pytest
from isort.exceptions import FormattingPluginDoesNotExist



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        formatter = 'my_formatter'
        with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
            raise FormattingPluginDoesNotExist(formatter)
>       assert str(exc_info.value) == f"Specified formatting plugin of {formatter} does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 48 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:9: AssertionError
_______________________________ test_none_input ________________________________

    def test_none_input():
        formatter = None
        with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
            raise FormattingPluginDoesNotExist(formatter)
>       assert str(exc_info.value) == f"Specified formatting plugin of {formatter} does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 40 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:15: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        formatter = 12345
        with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
            raise FormattingPluginDoesNotExist(formatter)
>       assert str(exc_info.value) == f"Specified formatting plugin of {formatter} does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 41 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_invalid_input
============================== 3 failed in 0.09s ===============================
"""