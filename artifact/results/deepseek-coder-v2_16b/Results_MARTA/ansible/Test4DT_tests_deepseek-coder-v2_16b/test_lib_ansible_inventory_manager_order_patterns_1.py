
import pytest
from ansible.inventory.manager import order_patterns

def test_valid_input():
    patterns = ['!exclude1', 'pattern2', '&intersect3']
    expected = ['pattern2', '&intersect3', '!exclude1']
    assert order_patterns(patterns) == expected

def test_empty_list():
    patterns = []
    expected = ['all']
    assert order_patterns(patterns) == expected

def test_only_intersection_and_exclusion():
    patterns = ['!exclude1', '&intersect3']
    expected = ['all', '&intersect3', '!exclude1']
    assert order_patterns(patterns) == expected
