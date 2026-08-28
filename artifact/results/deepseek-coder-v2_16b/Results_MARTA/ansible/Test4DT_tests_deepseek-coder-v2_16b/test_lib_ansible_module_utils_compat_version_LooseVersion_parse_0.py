
import pytest
from ansible.module_utils.compat.version import LooseVersion



def test_valid_input():
    version = LooseVersion("1.5.2b2")
    assert version.version == [1, 5, 2, 'b', 2]

def test_equal_versions():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b2")
    assert v1 == v2

def test_unequal_versions():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert v1 != v2

def test_compare_with_string():
    version = LooseVersion("1.5.2b2")
    assert version == "1.5.2b2"
