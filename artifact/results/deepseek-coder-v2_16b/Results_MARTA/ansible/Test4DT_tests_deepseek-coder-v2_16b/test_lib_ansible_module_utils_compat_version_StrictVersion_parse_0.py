
import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_invalid_input():
    with pytest.raises(ValueError):
        StrictVersion('invalid_version')

def test_comparison_lesser():
    v1 = StrictVersion('0.5a1')
    v2 = StrictVersion('0.5b3')
    assert v1 < v2, f"Expected 0.5a1 to be less than 0.5b3 but got {v1} and {v2}"

def test_comparison_equal():
    v1 = StrictVersion('0.5a1')
    v2 = StrictVersion('0.5a1')
    assert v1 == v2, f"Expected 0.5a1 to be equal to 0.5a1 but got {v1} and {v2}"