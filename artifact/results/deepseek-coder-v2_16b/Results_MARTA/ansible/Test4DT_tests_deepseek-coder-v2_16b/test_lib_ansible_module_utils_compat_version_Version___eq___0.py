
from lib.ansible.module_utils.compat.version import StrictVersion, LooseVersion
import pytest



def test_strict_version_valid():
    v = StrictVersion('1.0.4b1')
    assert str(v) == '1.0.4b1'

def test_loose_version_valid():
    v = LooseVersion("1.5.2b2")
    assert str(v) == "1.5.2b2"

def test_strict_version_equality():
    v1 = StrictVersion('0.5a1')
    v2 = StrictVersion('0.5a1')
    assert v1 == v2

def test_loose_version_inequality():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert v1 != v2