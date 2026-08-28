
import pytest
from ansible.utils.version import SemanticVersion

# Test creating a SemanticVersion instance with valid version string
def test_valid_version_creation():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3

# Test raising ValueError for invalid version string
def test_invalid_version_string():
    with pytest.raises(ValueError):
        SemanticVersion('invalid-version')

# Test comparing two versions
def test_version_comparison():
    version1 = SemanticVersion('2.0.0-alpha')
    version2 = SemanticVersion('1.99.99')
    assert version1 > version2
