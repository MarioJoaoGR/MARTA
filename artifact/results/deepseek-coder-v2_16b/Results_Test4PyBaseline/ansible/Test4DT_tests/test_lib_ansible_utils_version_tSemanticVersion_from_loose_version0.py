
import pytest
from ansible.utils.version import SemanticVersion, LooseVersion
import re

# Test cases for the SemanticVersion class
def test_semantic_version_creation():
    semver = SemanticVersion("1.2.3")
    assert str(semver) == "1.2.3"

def test_semantic_version_prerelease():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert str(semver_pre) == "1.2.3-beta.1"

def test_semantic_version_comparison():
    semver = SemanticVersion("1.2.3")
    semver3 = SemanticVersion("2.0.0")
    assert semver < semver3
    
    semver4 = SemanticVersion("1.2.3-alpha.1")
    assert not (semver == semver4)  # Fixed the comparison operator to '=='

# Test cases for the from_loose_version method
def test_from_loose_version():
    loose_version = LooseVersion("1.2.3")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert str(semver) == "1.2.3"

def test_invalid_loose_version():
    with pytest.raises(ValueError):
        loose_version = "invalid_version"
        SemanticVersion.from_loose_version(loose_version)
