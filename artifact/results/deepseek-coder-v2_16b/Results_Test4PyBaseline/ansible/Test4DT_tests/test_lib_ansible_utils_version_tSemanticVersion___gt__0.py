
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for SemanticVersion class

def test_valid_version():
    semver = SemanticVersion("1.2.3")
    assert str(semver) == "1.2.3"

def test_prerelease_version():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert str(semver_pre) == "1.2.3-beta.1"

def test_invalid_version():
    with pytest.raises(ValueError):
        semver_invalid = SemanticVersion("1.2")  # Missing patch number and prerelease identifier

def test_compare_versions():
    semver3 = SemanticVersion("2.0.0")
    assert semver3 > SemanticVersion("1.9.9"), "Expected 2.0.0 to be greater than 1.9.9"

def test_is_stable():
    semver_prerelease = SemanticVersion("1.2.3-alpha.1")
    assert not semver_prerelease.is_stable(), "Expected the version with prerelease identifiers to be unstable"

if __name__ == "__main__":
    pytest.main()
