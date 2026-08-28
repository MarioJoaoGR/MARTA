
import pytest
from ansible.utils.version import SemanticVersion

# Test valid version strings
def test_valid_case_1():
    v1 = SemanticVersion('1.2.3')
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3

def test_valid_case_2():
    v2 = SemanticVersion('1.0.0-alpha.1')
    assert v2.prerelease == ('alpha', '1')

def test_valid_case_3():
    v3 = SemanticVersion('1.0.0+build123')
    assert v3.buildmetadata == ('build', '123')

# Test error handling for invalid version strings
def test_edge_case_none():
    try:
        v = SemanticVersion(None)
    except ValueError as e:
        assert str(e) == "Invalid version string"

def test_error_case():
    try:
        v = SemanticVersion('invalid-version')
    except ValueError as e:
        assert str(e) == "Invalid version string"
