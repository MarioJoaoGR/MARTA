
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for SemanticVersion class initialization and parsing

def test_valid_version():
    semver = SemanticVersion("1.2.3")
    assert semver.vstring == "1.2.3"
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

def test_valid_version_with_prerelease():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert semver_pre.vstring == "1.2.3-beta.1"
    assert semver_pre.major == 1
    assert semver_pre.minor == 2
    assert semver_pre.patch == 3
    assert semver_pre.prerelease == ("beta", "1")
    assert semver_pre.buildmetadata == ()

def test_invalid_version():
    with pytest.raises(ValueError):
        SemanticVersion("1.2")  # Missing patch number and prerelease identifier

# Test cases for version comparison

def test_version_comparison():
    semver = SemanticVersion("1.2.3")
    semver_larger = SemanticVersion("2.0.0")
    assert (semver < semver_larger) is True

def test_prerelease_comparison():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    semver_stable = SemanticVersion("2.0.0")
    assert (semver_pre < semver_stable) is True

# Test cases for checking if a version is stable or not

def test_is_stable():
    semver_stable = SemanticVersion("1.2.3")
    assert semver_stable.is_stable() is True

def test_is_not_stable():
    semver_prerelease = SemanticVersion("1.2.3-alpha.1")
    assert semver_prerelease.is_stable() is False

# Test cases for invalid version strings

def test_invalid_version_string():
    with pytest.raises(ValueError):
        SemanticVersion("invalid_version_string")
