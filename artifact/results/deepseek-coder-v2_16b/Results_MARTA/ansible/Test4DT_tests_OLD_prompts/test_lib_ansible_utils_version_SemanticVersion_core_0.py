
import pytest
from ansible.utils.version import SemanticVersion

def test_valid_version():
    v1 = SemanticVersion("1.2.3")
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3




def test_compare_versions():
    version1 = SemanticVersion('2.0.0-alpha')
    version2 = SemanticVersion('1.99.99')
    assert version1 > version2