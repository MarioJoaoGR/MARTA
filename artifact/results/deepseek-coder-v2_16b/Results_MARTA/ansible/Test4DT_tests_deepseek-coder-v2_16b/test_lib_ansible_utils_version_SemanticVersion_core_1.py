
import pytest
from ansible.utils.version import SemanticVersion

# Test Scenario 1: Parsing a valid version string
def test_valid_version_string():
    version = SemanticVersion("1.2.3")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == ()
    assert version.buildmetadata == ()

# Test Scenario 2: Parsing a version string with prerelease and build metadata

# Test Scenario 3: Parsing a version string with only major, minor, and patch
def test_version_only_major_minor_patch():
    version = SemanticVersion("2.1.4")
    assert version.major == 2
    assert version.minor == 1
    assert version.patch == 4
    assert version.prerelease == ()
    assert version.buildmetadata == ()

# Test Scenario 4: Parsing a version string with prerelease but no build metadata

# Test Scenario 5: Parsing a version string with build metadata but no prerelease

# Test Scenario 6: Parsing a version string with both prerelease and build metadata

# Test Scenario 7: Parsing an invalid version string should raise ValueError
def test_invalid_version_string():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-version")