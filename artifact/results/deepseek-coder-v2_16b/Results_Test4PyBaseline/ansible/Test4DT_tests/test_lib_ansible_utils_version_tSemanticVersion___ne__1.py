
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for SemanticVersion class

def test_ne_with_different_major():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("2.0.0")
    assert (semver1 != semver2) is True

def test_ne_with_different_minor():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("1.3.0")
    assert (semver1 != semver2) is True

def test_ne_with_different_patch():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("1.2.4")
    assert (semver1 != semver2) is True

def test_ne_with_different_prerelease():
    semver1 = SemanticVersion("1.2.3-beta.1")
    semver2 = SemanticVersion("1.2.3-gamma.1")
    assert (semver1 != semver2) is True

def test_ne_with_different_buildmetadata():
    semver1 = SemanticVersion("1.2.3+build1")
    semver2 = SemanticVersion("1.2.3+build2")