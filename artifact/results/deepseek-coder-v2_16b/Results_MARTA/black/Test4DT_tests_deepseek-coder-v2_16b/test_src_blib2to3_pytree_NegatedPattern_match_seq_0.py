
import pytest
import re
from typing import Optional, Any

# Assuming BasePattern is defined somewhere in a module or imported correctly
class BasePattern:
    pass

class NegatedPattern:
    def __init__(self, content: Optional[Any] = None) -> None:
        if content is not None:
            assert isinstance(content, BasePattern), repr(content)
        self.content = content

    def match_seq(self, nodes, results=None) -> bool:
        return len(nodes) == 0

# Test scenarios for NegatedPattern class


def test_invalid_input():
    with pytest.raises(AssertionError):
        np = NegatedPattern(content='not a pattern')

# Additional tests can be added here following the same structure and principles