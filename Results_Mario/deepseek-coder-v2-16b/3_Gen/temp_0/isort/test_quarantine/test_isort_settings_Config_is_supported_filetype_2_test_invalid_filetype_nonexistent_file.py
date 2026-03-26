
import os
from isort import settings
from isort.config import Config
import pytest

@pytest.mark.parametrize("file_name", ["non_existent_file.py"])
def test_invalid_filetype_nonexistent_file(file_name):
    config = Config()
    assert not config.is_supported_filetype(file_name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_is_supported_filetype_2_test_invalid_filetype_nonexistent_file
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_2_test_invalid_filetype_nonexistent_file.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_2_test_invalid_filetype_nonexistent_file.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""