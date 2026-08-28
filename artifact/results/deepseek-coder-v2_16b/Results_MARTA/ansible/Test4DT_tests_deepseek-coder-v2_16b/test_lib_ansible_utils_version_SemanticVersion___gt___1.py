
import pytest
from ansible.utils.version import SemanticVersion

# Test valid input happy path
def test_valid_input_happy_path():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    
    v2 = SemanticVersion('1.0.0-alpha.1')
    assert v2.prerelease == ('alpha', '1')
    
    v3 = SemanticVersion('1.0.0+build123')
    assert v3.buildmetadata == ('build', '123')

# Test edge cases with None, empty strings, and invalid formats
def test_edge_cases():
    with pytest.raises(ValueError):
        SemanticVersion(None)
    
    with pytest.raises(ValueError):
        SemanticVersion('')
    
    with pytest.raises(ValueError):
        SemanticVersion('invalid-format')

# Test raising ValueError for invalid version strings
def test_error_handling():
    try:
        SemanticVersion('invalid-format')
    except ValueError as e:
        assert str(e) == "Invalid semantic version string 'invalid-format'"
