
import pytest
from ansible.utils.version import _Alpha

def test_valid_comparison():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    assert alpha1 == alpha2, "Instances with the same specifier should be equal"
