
import pytest
from ansible.utils.version import SemanticVersion


def test_specific_components():
    with pytest.raises(TypeError):
        SemanticVersion(major=1, minor=2, patch=3, prerelease=('alpha', '1'), buildmetadata=('build', '123'))