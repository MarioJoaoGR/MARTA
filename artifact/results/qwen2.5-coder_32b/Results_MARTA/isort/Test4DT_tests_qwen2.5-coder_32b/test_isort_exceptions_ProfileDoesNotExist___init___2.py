
import pytest

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

# Test cases
def test_valid_case():
    global profiles
    profiles = ['user', 'guest', 'superuser']
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist('admin')
    assert str(excinfo.value) == "Specified profile of admin does not exist. Available profiles: user,guest,superuser."

def test_edge_case_none_profile():
    global profiles
    profiles = ['user', 'guest', 'superuser']
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist(None)
    assert str(excinfo.value) == "Specified profile of None does not exist. Available profiles: user,guest,superuser."

def test_invalid_case_empty_profiles():
    global profiles
    profiles = []
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist('admin')
    assert str(excinfo.value) == "Specified profile of admin does not exist. Available profiles: ."
