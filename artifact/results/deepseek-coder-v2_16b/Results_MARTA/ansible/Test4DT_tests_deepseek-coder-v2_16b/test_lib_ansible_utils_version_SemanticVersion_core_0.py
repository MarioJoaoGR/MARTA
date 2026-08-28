
import pytest
from ansible.utils.version import SemanticVersion

# Test valid case scenario
def test_valid_case():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3

# Test edge cases with None and empty strings
def test_edge_case():
    # Test with None
    with pytest.raises(ValueError):
        v2 = SemanticVersion(None)
    
    # Test with empty string
    with pytest.raises(ValueError):
        v3 = SemanticVersion('')

# Test raising ValueError for invalid input
def test_error_case():
    with pytest.raises(ValueError):
        v4 = SemanticVersion()
