
# Module: ansible.utils.version
from ansible.utils.version import _Alpha
import pytest

# Test cases for the `_Alpha` class
def test__alpha_init():
    alpha1 = _Alpha("test")
    assert alpha1.specifier == "test"
    
    alpha2 = _Alpha(5)
    assert str(alpha2.specifier) == '5'

def test__alpha_repr():
    alpha1 = _Alpha("test")
    assert repr(alpha1) == "'test'"
    
    alpha2 = _Alpha(5)
    assert repr(alpha2) == "5"
