
import pytest
from unittest.mock import patch, MagicMock
import subprocess
from isort.settings import Config

@pytest.mark.parametrize("folder", ["valid_git_folder", "invalid_folder"])
def test_error_case(folder):
    with patch('isort.settings.os.path.exists', return_value=True), \
         patch('isort.settings.subprocess.check_output', side_effect=subprocess.CalledProcessError(1, "git ls-files")):
        config = Config()
        with pytest.raises(subprocess.CalledProcessError):
            config._check_folder_git_ls_files(folder)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_error_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_error_case[valid_git_folder] _______________________

folder = 'valid_git_folder'

    @pytest.mark.parametrize("folder", ["valid_git_folder", "invalid_folder"])
    def test_error_case(folder):
        with patch('isort.settings.os.path.exists', return_value=True), \
             patch('isort.settings.subprocess.check_output', side_effect=subprocess.CalledProcessError(1, "git ls-files")):
            config = Config()
>           with pytest.raises(subprocess.CalledProcessError):
E           Failed: DID NOT RAISE <class 'subprocess.CalledProcessError'>

isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_error_case.py:12: Failed
_______________________ test_error_case[invalid_folder] ________________________

folder = 'invalid_folder'

    @pytest.mark.parametrize("folder", ["valid_git_folder", "invalid_folder"])
    def test_error_case(folder):
        with patch('isort.settings.os.path.exists', return_value=True), \
             patch('isort.settings.subprocess.check_output', side_effect=subprocess.CalledProcessError(1, "git ls-files")):
            config = Config()
>           with pytest.raises(subprocess.CalledProcessError):
E           Failed: DID NOT RAISE <class 'subprocess.CalledProcessError'>

isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_error_case.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_error_case.py::test_error_case[valid_git_folder]
FAILED isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_error_case.py::test_error_case[invalid_folder]
============================== 2 failed in 0.12s ===============================
"""