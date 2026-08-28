
import pytest
from ansible.utils.version import SemanticVersion

# Test valid input - happy path
def test_valid_input_happy_path():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    assert not v1.is_prerelease()

# Test handling of None input
def test_edge_case_none():
    with pytest.raises(ValueError):
        v2 = SemanticVersion(None)

# Test raising ValueError with invalid version string
def test_invalid_input_error_handling():
    try:
        v3 = SemanticVersion('invalid-version')
    except ValueError as e:
        assert str(e) == "Invalid semantic version string 'invalid-version'"
