
import pytest
from blib2to3.pytree import WildcardPattern, HUGE


def test_wildcard_pattern_with_content():
    subpattern = "subpattern"
    pattern = WildcardPattern(content=[[subpattern]], min=1, max=HUGE)
    assert pattern.min == 1
    assert pattern.max == HUGE
    assert len(pattern.content) == 1
    assert pattern.content[0][0] == subpattern


