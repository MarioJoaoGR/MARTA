
import pytest
from lib.ansible.module_utils.compat.version import StrictVersion

# Test creation of a valid version object
def test_valid_version_creation():
    v = StrictVersion('1.2.3')
    assert str(v) == '1.2.3'

# Test creation of an invalid version object and expect ValueError
def test_invalid_version_creation():
    with pytest.raises(ValueError):
        v = StrictVersion('1.2a3')

# Test comparison of version objects with and without pre-release tags
def test_version_comparison():
    v1 = StrictVersion('1.2.3')
    v2 = StrictVersion('1.2.4')
    assert not (v1 == v2)  # False because '1.2.3' is less than '1.2.4'
    assert v1 < v2        # True because '1.2.3' is less than '1.2.4'
    assert v1 <= v2       # True because '1.2.3' is less than '1.2.4'
    assert not (v1 > v2)  # False because '1.2.3' is less than '1.2.4'
    assert not (v1 >= v2) # False because '1.2.3' is less than '1.2.4'
    
    v1 = StrictVersion('1.2.3b4')
    v2 = StrictVersion('1.2.3')
    assert not (v1 == v2)  # False because '1.2.3b4' is considered less than '1.2.3' due to the pre-release tag
    assert v1 < v2        # True because '1.2.3b4' is less than '1.2.3'
    assert v1 <= v2       # True because '1.2.3b4' is less than '1.2.3'
    assert not (v1 > v2)  # False because '1.2.3b4' is less than '1.2.3'
    assert not (v1 >= v2) # False because '1.2.3b4' is less than '1.2.3'
