
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_empty_case():
    maybe = Maybe(value=None, is_nothing=True)
    either = maybe.to_either()
    
    assert isinstance(either, Left)
    assert either.value == None
