
import pytest
from ansible.utils.version import LooseVersion
from SemanticVersion import SemanticVersion, from_loose_version

# Test valid input
def test_valid_input():
    semantic_version = SemanticVersion('1.2.3')
    assert semantic_version.major == 1
    assert semantic_version.minor == 2
    assert semantic_version.patch == 3

# Test handling of None input
def test_none_input():
    with pytest.raises(ValueError):
        SemanticVersion(None)

# Test raising ValueError with invalid version string
def test_invalid_input():
    with pytest.raises(ValueError):
        SemanticVersion('1.2')
