
import pytest
from pysnooper.utils import ensure_tuple

# Test valid inputs scenario

# Test edge cases scenario
def test_edge_cases():
    assert ensure_tuple(None) == (None,)
    assert ensure_tuple([]) == ()
    assert ensure_tuple({}) == tuple({})