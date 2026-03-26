
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    either_result = maybe_none.to_either()
    
    assert isinstance(either_result, Left)
    assert either_result.value == None
