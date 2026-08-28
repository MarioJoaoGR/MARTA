
import pytest
from ansible.utils.version import SemanticVersion

# Scenario 1: Test standard input with valid version strings
def test_valid_input_happy_path():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    assert not v1.is_prerelease()
    assert v1.is_stable()

# Scenario 2: Test edge cases including None, empty strings, and invalid formats
def test_edge_cases():
    with pytest.raises(ValueError):
        SemanticVersion(None)
    
    with pytest.raises(ValueError):
        SemanticVersion('')
    
    with pytest.raises(ValueError):
        SemanticVersion('invalid-version')

# Scenario 3: Test raising ValueError for invalid version strings
def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        v3 = SemanticVersion('invalid-version')
