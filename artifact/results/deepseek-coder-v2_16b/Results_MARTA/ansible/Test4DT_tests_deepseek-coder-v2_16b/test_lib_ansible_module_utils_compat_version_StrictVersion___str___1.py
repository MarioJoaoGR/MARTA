
import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_invalid_version():
    with pytest.raises(ValueError):
        StrictVersion('invalid')