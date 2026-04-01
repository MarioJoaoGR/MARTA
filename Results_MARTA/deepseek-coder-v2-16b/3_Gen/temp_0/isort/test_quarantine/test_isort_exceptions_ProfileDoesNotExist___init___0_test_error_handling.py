
import pytest
from isort.exceptions import ProfileDoesNotExist
from isort.profile import set_profile, profiles  # Assuming this module exists and contains the profile list

def test_error_handling():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        set_profile("non_existent_profile")
    
    assert str(excinfo.value) == f"Specified profile of non_existent_profile does not exist. Available profiles: {','.join(profiles)}."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_ProfileDoesNotExist___init___0_test_error_handling
isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_error_handling.py:4:0: E0401: Unable to import 'isort.profile' (import-error)
isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_error_handling.py:4:0: E0611: No name 'profile' in module 'isort' (no-name-in-module)


"""