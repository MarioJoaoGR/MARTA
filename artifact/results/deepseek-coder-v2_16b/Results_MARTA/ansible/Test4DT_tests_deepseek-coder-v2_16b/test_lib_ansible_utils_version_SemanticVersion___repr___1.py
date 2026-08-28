
import pytest
from ansible.utils.version import SemanticVersion

# Test for version without prerelease or buildmetadata
def test_version_without_prerelease_or_buildmetadata():
    v = SemanticVersion("1.2.3")
    assert v.major == 1
    assert v.minor == 2
    assert v.patch == 3
    assert v.prerelease == ()
    assert v.buildmetadata == ()

# Test for version with prerelease

# Test for version with buildmetadata

# Test for version with prerelease and buildmetadata