
import pytest
from your_module_name import SemanticVersion  # Replace 'your_module_name' with the actual module name where SemanticVersion is defined

# Test cases for valid input happy path
def test_valid_input_happy_path():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    
    v2 = SemanticVersion('1.0.0-alpha.1')
    assert v2.prerelease == ('alpha', '1')
    
    v3 = SemanticVersion('1.0.0+build123')
    assert v3.buildmetadata == ('build', '123')

# Test cases for edge cases with None, empty strings, and invalid formats
def test_edge_cases():
    with pytest.raises(ValueError):
        v_none = SemanticVersion(None)
    
    with pytest.raises(ValueError):
        v_empty = SemanticVersion('')
    
    with pytest.raises(ValueError):
        v_invalid = SemanticVersion('invalid')

# Test cases for raising ValueError for invalid version strings
def test_error_handling():
    with pytest.raises(ValueError) as e:
        SemanticVersion('invalid')
    assert str(e.value) == "Invalid semantic version string 'invalid'"
