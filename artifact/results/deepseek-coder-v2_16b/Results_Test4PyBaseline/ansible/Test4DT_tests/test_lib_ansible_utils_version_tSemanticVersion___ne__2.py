
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for SemanticVersion class

def test_ne_with_different_versions():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("2.0.0")
    assert semver1 != semver2

def test_ne_with_same_version():
    semver = SemanticVersion("1.2.3")
    same_semver = SemanticVersion("1.2.3")
    assert not (semver != same_semver)

def test_ne_with_different_prerelease_versions():
    semver1 = SemanticVersion("1.2.3-beta.1")
    semver2 = SemanticVersion("1.2.3-alpha.1")
    assert semver1 != semver2

def test_ne_with_same_prerelease_versions():
    semver = SemanticVersion("1.2.3-beta.1")
    same_semver = SemanticVersion("1.2.3-beta.1")
    assert not (semver != same_semver)

def test_ne_with_different_buildmetadata_versions():
    semver1 = SemanticVersion("1.2.3+build1")
    semver2 = SemanticVersion("1.2.3+build2")