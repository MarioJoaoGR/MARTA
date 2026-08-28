
import pytest
from your_module import order_patterns  # Replace 'your_module' with the actual module name where `order_patterns` is defined

# Test scenario 1: Valid input with valid patterns including exclusion, intersection, and regular patterns
def test_valid_input():
    patterns = ["!exclude1", "pattern2", "&intersect3"]
    expected = ["pattern2", "&intersect3", "!exclude1"]
    assert order_patterns(patterns) == expected

# Test scenario 2: Empty list of patterns
def test_empty_list():
    patterns = []
    expected = ['all']
    assert order_patterns(patterns) == expected

# Test scenario 3: List containing only intersection and exclusion patterns
def test_only_intersection_and_exclusion():
    patterns = ["!exclude1", "&intersect3"]
    expected = ['all', '&intersect3', '!exclude1']
    assert order_patterns(patterns) == expected
