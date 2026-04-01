
import pytest
from flutes.iterator import split_by
from typing import List, Iterable

def test_edge_case_empty_list():
    # Test splitting an empty list
    result = list(split_by([], criterion=lambda x: False))
    assert result == []
