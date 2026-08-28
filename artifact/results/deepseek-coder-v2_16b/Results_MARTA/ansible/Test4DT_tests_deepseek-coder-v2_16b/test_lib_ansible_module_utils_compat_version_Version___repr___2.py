
import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_valid_strict_version():
    v = StrictVersion('1.2.3')
    assert str(v) == '1.2.3'

def test_valid_strict_version_with_prerelease():
    v = StrictVersion('1.2.3b4')
    assert str(v) == '1.2.3b4'
