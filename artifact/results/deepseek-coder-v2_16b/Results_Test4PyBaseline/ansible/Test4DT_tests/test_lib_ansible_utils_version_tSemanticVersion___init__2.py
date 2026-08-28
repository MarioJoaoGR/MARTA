
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for SemanticVersion class initialization and parsing

def test_semantic_version_initialization():
    semver = SemanticVersion("1.2.3")
    assert semver.vstring == "1.2.3"
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

def test_semantic_version_initialization_with_prerelease():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert semver_pre.vstring == "1.2.3-beta.1"
    assert semver_pre.major == 1
    assert semver_pre.minor == 2
    assert semver_pre.patch == 3