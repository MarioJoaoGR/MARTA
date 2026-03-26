
import pytest
from pytutils.iters import dedupe_iter

def test_empty_input():
    data = []
    result = list(dedupe_iter(data))
    assert result == [], "Expected an empty list for empty input"
