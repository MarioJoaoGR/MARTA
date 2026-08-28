
import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_valid_version():
    v = LooseVersion("1.5.2b2")
    assert v.version == [1, 5, 2, 'b', 2]


def test_compare_versions():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert v1 < v2
    assert not (v1 == v2)

def test_default_constructor():
    v_default = LooseVersion()
    with pytest.raises(AttributeError):  # Since __init__ does not allow default construction without a parameter
        _ = v_default.version