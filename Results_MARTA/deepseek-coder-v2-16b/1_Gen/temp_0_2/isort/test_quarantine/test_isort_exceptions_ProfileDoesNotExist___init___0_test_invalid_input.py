
import pytest
from isort.exceptions import ProfileDoesNotExist
from isort.profile_reader import profiles, set_profile

def test_invalid_input():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        set_profile("non_existent_profile")
    
    assert str(excinfo.value) == "Specified profile of non_existent_profile does not exist. Available profiles: default,user1,user2."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_ProfileDoesNotExist___init___0_test_invalid_input
isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_invalid_input.py:4:0: E0401: Unable to import 'isort.profile_reader' (import-error)
isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_invalid_input.py:4:0: E0611: No name 'profile_reader' in module 'isort' (no-name-in-module)


"""