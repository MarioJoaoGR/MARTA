
import pytest
from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_str():
    v2 = LooseVersion("1.0.0-alpha.1")
    assert str(v2) == "1.0.0-alpha.1"

def test_loose_version_compare_equal():
    version1 = LooseVersion('1.0.0')
    version2 = LooseVersion('1.0.0')
    assert version1 == version2

def test_loose_version_compare_not_equal():
    version1 = LooseVersion('1.0.1')
    version2 = LooseVersion('1.0.0')
    assert version1 != version2

def test_loose_version_greater_than():
    version1 = LooseVersion('2.0.0')
    version2 = LooseVersion('1.99.99')
    assert version1 > version2

def test_loose_version_less_than():
    version1 = LooseVersion('1.0.0')
    version2 = LooseVersion('2.0.0')
    assert version1 < version2