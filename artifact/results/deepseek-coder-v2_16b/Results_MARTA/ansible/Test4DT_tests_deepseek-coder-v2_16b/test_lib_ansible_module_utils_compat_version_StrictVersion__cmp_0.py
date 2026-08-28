
import pytest
from ansible.module_utils.compat.version import StrictVersion



def test_invalid_version_string():
    with pytest.raises(ValueError):
        StrictVersion("1")