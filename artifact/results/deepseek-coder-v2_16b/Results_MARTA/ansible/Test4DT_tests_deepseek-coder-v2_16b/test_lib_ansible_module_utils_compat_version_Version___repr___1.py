
import pytest
from lib.ansible.module_utils.compat.version import StrictVersion

# Test creation of a valid version object
def test_valid_version_creation():
    v = StrictVersion('1.2.3')
    assert str(v) == '1.2.3'

# Test creation of an invalid version object, expecting ValueError
def test_invalid_version_creation():
    try:
        v = StrictVersion('1.2a3')
    except ValueError as e:
        assert str(e) == "invalid version number '1.2a3'"

# Test comparison of version objects, including valid and invalid comparisons
def test_version_comparison():
    v1 = StrictVersion('1.2.3')
    v2 = StrictVersion('1.2.4')
    assert not (v1 == v2)
    assert v1 < v2
    assert v1 <= v2
    assert not (v1 > v2)
    assert not (v1 >= v2)
