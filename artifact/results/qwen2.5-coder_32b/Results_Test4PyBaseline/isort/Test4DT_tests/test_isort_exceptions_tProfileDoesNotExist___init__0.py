
# Test case  
import pytest
from isort.exceptions import ProfileDoesNotExist

# Mock list of available profiles for testing purposes
profiles = ["black", "django", "pycharm", "google", "open_stack", "plone", "attrs", "hug", "wemake", "appnexus"]

def test_profile_does_not_exist_with_valid_profile():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist("user_profile")
    assert str(excinfo.value) == f"Specified profile of user_profile does not exist. Available profiles: {','.join(profiles)}."
    assert excinfo.value.profile == "user_profile"

def test_profile_does_not_exist_with_another_valid_profile():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist("manager")
    assert str(excinfo.value) == f"Specified profile of manager does not exist. Available profiles: {','.join(profiles)}."
    assert excinfo.value.profile == "manager"

def test_profile_does_not_exist_with_empty_profile_name():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist("")
    assert str(excinfo.value) == f"Specified profile of  does not exist. Available profiles: {','.join(profiles)}."
    assert excinfo.value.profile == ""

def test_profile_does_not_exist_with_whitespace_profile_name():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist("   ")