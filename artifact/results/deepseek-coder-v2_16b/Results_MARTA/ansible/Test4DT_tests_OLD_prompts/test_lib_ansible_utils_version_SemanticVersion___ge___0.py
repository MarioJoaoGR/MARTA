
import pytest
from ansible.utils.version import SemanticVersion

def test_valid_version():
    version = SemanticVersion("1.2.3")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == ()
    assert version.buildmetadata == ()



def test_invalid_input_error_handling():
    with pytest.raises(ValueError) as excinfo:
        SemanticVersion('invalid-version')
    assert str(excinfo.value) == "invalid semantic version 'invalid-version'"

def test_comparison_greater_equal():
    version1 = SemanticVersion("2.0.0")
    version2 = SemanticVersion("1.99.99")
    assert version1 >= version2