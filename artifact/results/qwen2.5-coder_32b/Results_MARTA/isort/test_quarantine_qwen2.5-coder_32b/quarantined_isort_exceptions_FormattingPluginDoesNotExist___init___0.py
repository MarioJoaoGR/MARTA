
import pytest
from isort.exceptions import FormattingPluginDoesNotExist



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________ test_FormattingPluginDoesNotExist___init___basic _______________

    def test_FormattingPluginDoesNotExist___init___basic():
        # Test basic functionality of the FormattingPluginDoesNotExist exception
        with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
            raise FormattingPluginDoesNotExist('invalid_plugin')
    
>       assert str(excinfo.value) == "Specified formatting plugin of invalid_plugin does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 50 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:10: AssertionError
__________ test_FormattingPluginDoesNotExist___init___another_plugin ___________

    def test_FormattingPluginDoesNotExist___init___another_plugin():
        # Test the exception with another plugin name
        with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
            raise FormattingPluginDoesNotExist('another_invalid_plugin')
    
>       assert str(excinfo.value) == "Specified formatting plugin of another_invalid_plugin does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 58 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:17: AssertionError
___________ test_FormattingPluginDoesNotExist___init___empty_string ____________

    def test_FormattingPluginDoesNotExist___init___empty_string():
        # Test the exception with an empty string
        with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
            raise FormattingPluginDoesNotExist('')
    
>       assert str(excinfo.value) == "Specified formatting plugin of  does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 36 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_FormattingPluginDoesNotExist___init___basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_FormattingPluginDoesNotExist___init___another_plugin
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_qwen2.5-coder_32b/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_FormattingPluginDoesNotExist___init___empty_string
============================== 3 failed in 0.10s ===============================
"""