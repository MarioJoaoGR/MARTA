
import pytest
from ansible.utils.version import SemanticVersion

# Test valid input - happy path
def test_valid_input_happy_path():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    assert v1.prerelease == ()
    assert v1.buildmetadata == ()

# Test edge cases - None, empty lists, and boundary values
def test_edge_cases():
    with pytest.raises(ValueError):
        SemanticVersion(None)
    
    with pytest.raises(ValueError):
        SemanticVersion('')
    
    with pytest.raises(ValueError):
        SemanticVersion('1.2')  # Missing patch number and prerelease/build metadata

# Test invalid input - error handling
def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        SemanticVersion('invalid-version-string')
