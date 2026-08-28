
import pytest
from ansible.inventory.manager import order_patterns


def test_order_patterns_empty_list():
    assert order_patterns([]) == ['all']

def test_order_patterns_only_regular_patterns():
    assert order_patterns(["pattern1", "pattern2", "pattern3"]) == ["pattern1", "pattern2", "pattern3"]

def test_order_patterns_only_intersection_patterns():
    assert order_patterns(["&intersect1", "&intersect2", "&intersect3"]) == ['all', '&intersect1', '&intersect2', '&intersect3']

def test_order_patterns_only_exclusion_patterns():
    assert order_patterns(["!exclude1", "!exclude2", "!exclude3"]) == ['all', '!exclude1', '!exclude2', '!exclude3']