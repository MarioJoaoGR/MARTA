
import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_valid_version():
    v = StrictVersion('0.5a1')
    assert str(v) == '0.5a1'

def test_no_prerelease():
    v = StrictVersion('0.9.6')
    assert str(v) == '0.9.6'

def test_invalid_version():
    with pytest.raises(ValueError):
        v = StrictVersion('1')
