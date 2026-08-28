
import pytest
from ansible.utils.version import SemanticVersion

# Test comparison between versions where self is less than other
def test_less_than():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("2.0.0")
    assert str(semver1) < str(semver2), f"Expected {str(semver1)} to be less than {str(semver2)}"

# Test comparison between versions where self is greater than other
def test_greater_than():
    semver1 = SemanticVersion("2.0.0")
    semver2 = SemanticVersion("1.2.3")
    assert str(semver1) > str(semver2), f"Expected {str(semver1)} to be greater than {str(semver2)}"

# Test comparison between versions where self is equal to other
def test_equal():
    semver1 = SemanticVersion("1.2.3")
    semver2 = SemanticVersion("1.2.3")
    assert str(semver1) == str(semver2), f"Expected {str(semver1)} to be equal to {str(semver2)}"

# Test comparison with a different prerelease version
def test_comparison_with_prerelease():
    semver1 = SemanticVersion("1.2.3-beta")
    semver2 = SemanticVersion("1.2.3")