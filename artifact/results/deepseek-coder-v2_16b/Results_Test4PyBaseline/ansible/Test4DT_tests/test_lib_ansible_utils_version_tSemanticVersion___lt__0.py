
import pytest
from ansible.utils.version import SemanticVersion

# Test initialization with a valid semantic version string
def test_valid_semantic_version():
    semver = SemanticVersion("1.2.3")
    assert str(semver) == "1.2.3"

# Test initialization with a prerelease version string
def test_prerelease_semantic_version():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert str(semver_pre) == "1.2.3-beta.1"

# Test comparison between versions
def test_comparison():
    semver = SemanticVersion("1.2.3")
    semver_larger = SemanticVersion("2.0.0")
    assert str(semver) < str(semver_larger)

# Test initialization with an invalid version string (should raise ValueError)
def test_invalid_version_string():
    with pytest.raises(ValueError):
        semver_invalid = SemanticVersion("1.2")  # Missing patch number and prerelease part
