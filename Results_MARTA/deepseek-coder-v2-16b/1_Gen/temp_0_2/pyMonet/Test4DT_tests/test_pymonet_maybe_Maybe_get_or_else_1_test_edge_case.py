
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    none_maybe = Maybe(value=None, is_nothing=True)
    empty_maybe = Maybe(value='', is_nothing=False)
    
    assert none_maybe.get_or_else("default_none") == "default_none"
    assert empty_maybe.get_or_else("default_empty") == ""
