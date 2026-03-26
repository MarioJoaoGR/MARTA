
import pytest
from isort.config import Config  # Importing from isort.settings

@pytest.mark.parametrize("file_name", [
    "test_file.py",
    "test_file.txt",
    "test_file.bak~",
    "/tmp/test_file.py"
])
def test_is_supported_filetype(file_name):
    config = Config()
    assert config.is_supported_filetype(file_name) == (
        file_name.endswith(".py") or 
        ("." in file_name and not file_name.endswith("~"))
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_is_supported_filetype_3_test_error_case_with_missing_lines
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_error_case_with_missing_lines.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_error_case_with_missing_lines.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""