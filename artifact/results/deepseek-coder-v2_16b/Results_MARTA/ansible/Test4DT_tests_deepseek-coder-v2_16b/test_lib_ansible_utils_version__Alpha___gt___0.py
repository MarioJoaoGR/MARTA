
import pytest
from ansible.utils.version import _Alpha

def test_alpha_comparison():
    alpha1 = _Alpha("2")
    alpha2 = _Alpha("3")
    assert alpha1 < alpha2, "Expected '2' to be less than '3'"

