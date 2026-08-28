
import pytest
from ansible.utils.version import SemanticVersion

# Test cases for the SemanticVersion class
def test_valid_semantic_version():
    semver = SemanticVersion("1.2.3")
    assert str(semver) == "1.2.3"

def test_prerelease_version():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert str(semver_pre) == "1.2.3-beta.1"

def test_version_comparison():
    semver = SemanticVersion("1.2.3")  # Corrected variable name to 'semver'
    semver3 = SemanticVersion("2.0.0")
    assert str(semver) < str(semver3)  # True, because 1.x is less than 2.x

def test_check_prerelease():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    assert not semver_pre.is_stable()  # Outputs: False (since it's a prerelease)

def test_different_prerelease_comparison():
    semver_pre = SemanticVersion("1.2.3-beta.1")
    semver4 = SemanticVersion("1.2.3-alpha.1")
    assert str(semver_pre) != str(semver4)  # False, because they are different prerelease versions
