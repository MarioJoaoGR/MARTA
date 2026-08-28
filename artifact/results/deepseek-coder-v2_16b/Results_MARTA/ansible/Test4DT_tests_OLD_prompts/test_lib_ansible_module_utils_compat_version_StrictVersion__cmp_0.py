
import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_strict_version_cmp_equal():
    v1 = StrictVersion("1.0.4a3")
    v2 = StrictVersion("1.0.4b1")
    assert v1 != v2, "StrictVersion comparison should not be equal due to pre-release tags"

def test_strict_version_cmp_equal():
    v1 = StrictVersion("1.0.4a3")
    v2 = StrictVersion("1.0.4b1")
    assert str(v1) == "1.0.4a3"
    assert str(v2) == "1.0.4b1"
    assert v1 != v2, "StrictVersion comparison should not be equal due to pre-release tags"