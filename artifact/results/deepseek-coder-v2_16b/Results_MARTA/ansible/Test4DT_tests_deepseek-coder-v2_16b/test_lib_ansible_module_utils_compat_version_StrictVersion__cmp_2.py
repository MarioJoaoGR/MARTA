
import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_equal_versions():
    version1 = StrictVersion('1.0.4a3')
    version2 = StrictVersion('1.0.4a3')
    assert version1._cmp(version2) == 0

def test_lesser_version():
    version1 = StrictVersion('1.0.3')
    version2 = StrictVersion('1.0.4a3')
    assert version1._cmp(version2) < 0

def test_greater_version():
    version1 = StrictVersion('1.0.5')
    version2 = StrictVersion('1.0.4a3')
    assert version1._cmp(version2) > 0