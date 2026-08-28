
import pytest
from blib2to3.pytree import WildcardPattern

HUGE = 2147483647  # HUGE is a placeholder for the largest possible integer value


def test_valid_case_with_content():
    subpattern1 = "subpattern1"
    subpattern2 = "subpattern2"
    content = [[subpattern1, subpattern2]]
    pattern = WildcardPattern(content=content)
    assert pattern.min == 0
    assert pattern.max == HUGE
    assert pattern.name is None
    assert pattern.content == ((subpattern1, subpattern2),)

def test_valid_case_with_specific_values():
    specific_nodes = ["node1", "node2"]
    pattern = WildcardPattern(content=[specific_nodes], min=1, max=2)
    assert pattern.min == 1
    assert pattern.max == 2
    assert pattern.name is None
    assert pattern.content == (("node1", "node2"),)