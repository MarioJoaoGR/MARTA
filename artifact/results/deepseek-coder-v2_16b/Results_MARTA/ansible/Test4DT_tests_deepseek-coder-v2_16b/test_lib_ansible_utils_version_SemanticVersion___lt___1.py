
import pytest
from ansible.utils.version import SemanticVersion

# Test Scenario 1: Parsing a version string without prerelease or buildmetadata
def test_version_without_prerelease_or_buildmetadata():
    v = SemanticVersion("1.2.3")
    assert v.major == 1
    assert v.minor == 2
    assert v.patch == 3
    assert v.prerelease == ()
    assert v.buildmetadata == ()

# Test Scenario 2: Parsing a version string with prerelease

# Test Scenario 3: Parsing a version string with buildmetadata

# Test Scenario 4: Parsing a version string with both prerelease and buildmetadata