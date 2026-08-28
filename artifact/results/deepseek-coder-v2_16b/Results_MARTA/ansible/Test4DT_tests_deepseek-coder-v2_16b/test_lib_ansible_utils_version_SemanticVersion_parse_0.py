
import pytest
from ansible.utils.version import SemanticVersion

# Test valid input scenario
def test_valid_input():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    assert v1.prerelease == ()
    assert v1.buildmetadata == ()

# Test edge case scenario with None input
def test_edge_case():
    with pytest.raises(ValueError):
        v2 = SemanticVersion(None)

# Test invalid input scenario that should raise ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        try:
            v3 = SemanticVersion('invalid-version')
        except ValueError as e:
            assert str(e) == "invalid semantic version 'invalid-version'"
