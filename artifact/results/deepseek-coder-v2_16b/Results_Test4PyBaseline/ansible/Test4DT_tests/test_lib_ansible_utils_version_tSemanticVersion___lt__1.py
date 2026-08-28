
import pytest
from ansible.utils.version import SemanticVersion

# Test case for comparing two equal semantic versions
def test_equal_versions():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("1.2.3")
    assert not (semver1 < semver2), "Versions should be considered equal"  # Should return False because they are equal

# Test case for comparing a smaller version with a larger one
def test_smaller_version():
    semver_small = SemanticVersion("1.0.0")
    semver_large = SemanticVersion("2.0.0")
    assert semver_small < semver_large, "Smaller version should be less than the larger one"  # Should return True because 1.0.0 is less than 2.0.0

# Test case for comparing a larger version with a smaller one
def test_larger_version():
    semver_large = SemanticVersion("2.0.0")
    semver_small = SemanticVersion("1.0.0")
    assert not (semver_large < semver_small), "Larger version should not be less than the smaller one"  # Should return False because 2.0.0 is greater than 1.0.0

# Test case for comparing versions with different major numbers
def test_different_major():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("2.0.0")
    assert semver1 < semver2, "Versions with different majors should be compared by their major number"  # Should return True because 1.x is less than 2.x for any z

# Test case for comparing versions with different minor numbers
def test_different_minor():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("1.3.0")
    assert semver1 < semver2, "Versions with different minors should be compared by their minor number"  # Should return True because 1.2 is less than 1.3 for any z

# Test case for comparing versions with different patch numbers
def test_different_patch():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("1.2.4")
    assert semver1 < semver2, "Versions with different patches should be compared by their patch number"  # Should return True because 1.2.3 is less than 1.2.4

# Test case for comparing versions with different prerelease tags
def test_different_prerelease():
    semver1 = SemanticVersion("1.2.3-beta")
    semver2 = SemanticVersion("1.2.3-alpha")