
import pytest
from lib.ansible.module_utils.compat.version import StrictVersion, LooseVersion, SemanticVersion

# Test cases for StrictVersion
def test_valid_case_strict_version():
    v1 = StrictVersion('0.5a1')
    assert str(v1) == '0.5a1'

def test_edge_case_strict_version():
    with pytest.raises(ValueError):
        v2 = StrictVersion(None)
    with pytest.raises(ValueError):
        v2 = StrictVersion('')

def test_invalid_case_strict_version():
    with pytest.raises(ValueError):
        v3 = StrictVersion('invalid-version')

# Test cases for LooseVersion
def test_valid_case_loose_version():
    v1 = LooseVersion('1.5.2b2')
    assert str(v1) == '1.5.2b2'

def test_edge_case_loose_version():
    with pytest.raises(ValueError):
        v2 = LooseVersion(None)
    with pytest.raises(ValueError):
        v2 = LooseVersion('')

def test_invalid_case_loose_version():
    with pytest.raises(ValueError):
        v3 = LooseVersion('invalid-version')

# Test cases for SemanticVersion
def test_valid_case_semantic_version():
    v1 = SemanticVersion(major=2, minor=0, patch=0, prerelease='alpha')
    assert str(v1) == '2.0.0-alpha'

def test_edge_case_semantic_version():
    with pytest.raises(ValueError):
        v2 = SemanticVersion(None)
    with pytest.raises(ValueError):
        v2 = SemanticVersion('')

def test_invalid_case_semantic_version():
    with pytest.raises(ValueError):
        v3 = SemanticVersion('invalid-version')
