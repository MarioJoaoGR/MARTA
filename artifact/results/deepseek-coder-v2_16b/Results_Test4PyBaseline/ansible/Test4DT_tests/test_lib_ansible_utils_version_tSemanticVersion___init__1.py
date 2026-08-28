
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for SemanticVersion class initialization and parsing

@pytest.fixture
def semver():
    return SemanticVersion()

def test_init_without_vstring(semver):
    assert semver.vstring is None
    assert semver.major is None
    assert semver.minor is None
    assert semver.patch is None
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

def test_init_with_invalid_vstring():
    with pytest.raises(ValueError):
        SemanticVersion("1.2")  # Missing patch number and prerelease identifier

def test_parse_valid_version(semver):
    semver.parse("1.2.3")