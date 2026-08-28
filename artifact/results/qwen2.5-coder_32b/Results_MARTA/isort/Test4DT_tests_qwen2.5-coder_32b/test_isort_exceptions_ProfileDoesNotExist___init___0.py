
import pytest

# Define the list of available profiles globally
profiles = ["user", "guest", "superuser"]

class ProfileDoesNotExist(Exception):
    """
    Raised when a profile is set by the user that doesn't exist.
    """
    def __init__(self, profile: str):
        super().__init__(
            f"Specified profile of {profile} does not exist. "
            f"Available profiles: {','.join(profiles)}."
        )
        self.profile = profile

def check_profile_exists(profile_name):
    if profile_name not in profiles:
        raise ProfileDoesNotExist(profile_name)

def test_valid_case():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        check_profile_exists("admin")
    assert str(excinfo.value) == "Specified profile of admin does not exist. Available profiles: user,guest,superuser."

def test_edge_case_none():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        check_profile_exists(None)
    assert str(excinfo.value) == "Specified profile of None does not exist. Available profiles: user,guest,superuser."

def test_invalid_case_empty_string():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        check_profile_exists("")
    assert str(excinfo.value) == "Specified profile of  does not exist. Available profiles: user,guest,superuser."
