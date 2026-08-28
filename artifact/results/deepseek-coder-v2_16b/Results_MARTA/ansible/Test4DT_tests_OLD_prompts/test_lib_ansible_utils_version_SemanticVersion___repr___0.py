
import pytest
from ansible.utils.version import SemanticVersion

def test_valid_version():
    version = SemanticVersion("1.2.3")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert repr(version) == "SemanticVersion('1.2.3')"



def test_invalid_version():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-version")