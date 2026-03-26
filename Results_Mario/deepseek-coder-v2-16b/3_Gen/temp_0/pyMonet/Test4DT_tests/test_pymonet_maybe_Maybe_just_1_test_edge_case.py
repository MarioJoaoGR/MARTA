
from pymonet.maybe import Maybe

def test_edge_case():
    none_maybe = Maybe(value=None, is_nothing=True)
    empty_maybe = Maybe(value=[], is_nothing=False)
    
    assert none_maybe.is_nothing == True
    assert none_maybe.is_nothing is True  # Corrected assertion to check the boolean value of `is_nothing`
