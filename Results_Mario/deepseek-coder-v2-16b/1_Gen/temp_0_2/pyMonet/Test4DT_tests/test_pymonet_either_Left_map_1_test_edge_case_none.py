
import pytest
from pymonet.either import Left

def test_edge_case_none():
    left_value = Left(None)
    assert isinstance(left_value, Left)
    assert left_value.map(lambda x: x) == Left(None)
