
import pytest
from ansible.module_utils.compat.version import StrictVersion
import re

# Test valid version strings
def test_valid_input():
    version = StrictVersion('1.0.4a3')
    assert str(version) == '1.0.4a3'
    assert version.version == (1, 0, 4)
    assert version.prerelease == ('a', 3)

# Test invalid version strings and error handling
def test_invalid_input():
    with pytest.raises(ValueError):
        StrictVersion('invalid_version')

# Test comparison between versions with and without pre-release tags
def test_comparison():
    v1 = StrictVersion('0.5a1')
    v2 = StrictVersion('0.5b3')
    assert v1 < v2
    assert not (v1 > v2)
    assert not (v1 == v2)
