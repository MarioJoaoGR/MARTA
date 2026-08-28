
from lib.ansible.module_utils.compat.version import StrictVersion
import pytest

def test_strict_version_valid():
    v1 = StrictVersion('0.5a1')
    assert str(v1) == '0.5a1'

def test_strict_version_invalid():
    with pytest.raises(ValueError):
        v2 = StrictVersion('invalid-version')
