
import pytest
from ansible.utils.version import _Alpha

# Test cases for _Alpha class
def test_alpha_comparison():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("testing")
    alpha3 = _Alpha("a")
    
    assert not (alpha1 == alpha2), "Expected alpha1 and alpha2 to be not equal"
    assert alpha1 == "test", "Expected alpha1 to be equal to the string 'test'"