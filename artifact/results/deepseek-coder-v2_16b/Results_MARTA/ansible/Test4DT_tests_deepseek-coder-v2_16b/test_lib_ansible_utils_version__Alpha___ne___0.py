
import pytest
from ansible.utils.version import _Alpha

def test_valid_string_comparison():
    alpha1 = _Alpha("2")
    alpha2 = _Alpha("3")
    assert alpha1 < alpha2, "Expected string comparison to work as integer conversion"
