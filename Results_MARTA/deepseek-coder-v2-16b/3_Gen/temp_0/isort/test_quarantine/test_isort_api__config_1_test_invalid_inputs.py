
from pathlib import Path
from isort.api import _config, DEFAULT_CONFIG, Config
import pytest

@pytest.mark.parametrize("invalid_input", [None, "invalid_path"])
def test_invalid_inputs(invalid_input):
    with pytest.raises(ValueError) as excinfo:
        if invalid_input is None:
            _config()
        else:
            _config(settings_path=invalid_input)
    
    assert "You can either specify custom configuration options using kwargs or passing in a Config object." in str(excinfo.value)

@pytest.mark.parametrize("profile, expected_exception", [
    ("nonexistent_profile", pytest.raises(ProfileDoesNotExist)),
])
def test_invalid_profile(profile, expected_exception):
    with expected_exception:
        _config(profile=profile)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__config_1_test_invalid_inputs
isort/Test4DT_tests/test_isort_api__config_1_test_invalid_inputs.py:17:42: E0602: Undefined variable 'ProfileDoesNotExist' (undefined-variable)


"""