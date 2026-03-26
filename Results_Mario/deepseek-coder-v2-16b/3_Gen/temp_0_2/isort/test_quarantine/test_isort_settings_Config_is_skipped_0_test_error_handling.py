
import pytest
from isort.settings import Config

def test_config_with_invalid_profile():
    with pytest.raises(ProfileDoesNotExist):
        Config(config=None, profile="non_existent_profile")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_is_skipped_0_test_error_handling
isort/Test4DT_tests/test_isort_settings_Config_is_skipped_0_test_error_handling.py:6:23: E0602: Undefined variable 'ProfileDoesNotExist' (undefined-variable)


"""