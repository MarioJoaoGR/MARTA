
import pytest
from ansible.utils.version import SemanticVersion

# Test for version parsing without prerelease and buildmetadata
def test_version_without_prerelease_and_build():
    v = SemanticVersion("1.2.3")
    assert v.major == 1
    assert v.minor == 2
    assert v.patch == 3
    assert v.prerelease == ()
    assert v.buildmetadata == ()

# Test for version parsing with prerelease and without buildmetadata

# Test for version parsing with buildmetadata and without prerelease

# Test for version parsing with prerelease and buildmetadata

# Test for initializing with specific components