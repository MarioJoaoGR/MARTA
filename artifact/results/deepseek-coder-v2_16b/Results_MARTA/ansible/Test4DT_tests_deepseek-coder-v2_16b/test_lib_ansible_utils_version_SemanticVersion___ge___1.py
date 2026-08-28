
import pytest
from ansible.utils.version import SemanticVersion

def test_valid_input_happy_path():
    v1 = SemanticVersion("1.2.3")
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    
    v2 = SemanticVersion("1.0.0-alpha.1")
    assert v2.prerelease == ('alpha', '1')
    
    v3 = SemanticVersion("1.0.0+build123")
    assert v3.buildmetadata == ('build', '123')

def test_edge_cases():
    with pytest.raises(ValueError):
        v_none = SemanticVersion(None)
    
    with pytest.raises(ValueError):
        v_empty = SemanticVersion("")
    
    with pytest.raises(ValueError):
        v_invalid_format = SemanticVersion("1.2-alpha+build")

def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        v_invalid_str = SemanticVersion("invalid-version")
