
from lib.ansible.module_utils.compat.version import StrictVersion, Version
import pytest


def test_valid_comparison_with_same_strict_version():
    v1 = StrictVersion('1.0')
    v2 = StrictVersion('1.0')
    assert v1 >= v2, "Expected equality for versions with the same value"

def test_valid_comparison_with_greater_strict_version():
    v1 = StrictVersion('2.0')
    v2 = StrictVersion('1.0')
    assert v1 >= v2, "Expected greater than comparison for version 2.0 vs 1.0"
