
import pytest
from ansible.utils.version import SemanticVersion



def test_valid_without_prerelease_and_buildmetadata():
    v = SemanticVersion('1.2.3')
    assert v.major == 1
    assert v.minor == 2
    assert v.patch == 3
    assert v.prerelease == ()

def test_invalid_version_string():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-version")