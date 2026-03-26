
import pytest
from pymonet.either import Left

def test_edge_case():
    left_none_value = Left(None)
    assert isinstance(left_none_value, Left)
    assert left_none_value.map(lambda x: x) == Left(None)
