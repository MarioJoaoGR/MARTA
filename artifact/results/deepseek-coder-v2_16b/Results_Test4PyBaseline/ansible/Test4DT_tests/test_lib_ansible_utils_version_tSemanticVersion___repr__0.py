
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for the SemanticVersion class

def test_create_semantic_version():
    semver = SemanticVersion("1.2.3")
    assert str(semver) == "SemanticVersion('1.2.3')"

def test_create_semantic_version_with_meta():
    semver_with_meta = SemanticVersion("1.2.3-beta.1+build.123")
    assert str(semver_with_meta) == "SemanticVersion('1.2.3-beta.1+build.123')"