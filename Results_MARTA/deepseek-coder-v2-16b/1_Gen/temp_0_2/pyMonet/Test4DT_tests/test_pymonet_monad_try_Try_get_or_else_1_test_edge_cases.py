
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, False)
    assert none_try.get_or_else("default_none") == "default_none"
    
    # Test with empty string value
    empty_try = Try('', False)
    assert empty_try.get_or_else("default_empty") == "default_empty"
