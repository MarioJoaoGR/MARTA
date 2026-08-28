
import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_valid_version():
    v1 = LooseVersion("1.5.2b2")
    assert str(v1) == "1.5.2b2"


def test_comparison_equal():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b2")
    assert v1 == v2

def test_comparison_not_equal():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert not (v1 == v2)

def test_comparison_less_than():
    v1 = LooseVersion("1.5.2b2")
    v2 = LooseVersion("1.5.2b3")
    assert v1 < v2

def test_comparison_greater_than():
    v1 = LooseVersion("1.5.2b3")
    v2 = LooseVersion("1.5.2b2")
    assert v1 > v2

def test_repr_method():
    v1 = LooseVersion("1.5.2b2")
    assert repr(v1) == "LooseVersion ('1.5.2b2')"