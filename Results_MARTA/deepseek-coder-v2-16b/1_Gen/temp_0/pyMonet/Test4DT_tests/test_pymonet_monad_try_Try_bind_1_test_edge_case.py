
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    # Test with None input
    none_try = Try(None, False)
    assert none_try.bind(lambda x: Try(x + " bound", True)).value == Try(None, False).value
    
    # Test with empty list input
    empty_list_try = Try([], False)
    assert empty_list_try.bind(lambda x: Try(x + " bound", True)).value == Try([], False).value
