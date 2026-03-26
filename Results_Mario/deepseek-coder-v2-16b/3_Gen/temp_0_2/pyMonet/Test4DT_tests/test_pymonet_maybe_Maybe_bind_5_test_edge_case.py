
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    maybe_none = Maybe(value=None, is_nothing=True)
    
    # Test bind method with a mapper function that returns an empty Maybe if the value is None
    def mapper_function(x):
        return Maybe.nothing()
    
    result = maybe_none.bind(mapper_function)
    
    # Assert that the result is an instance of Maybe and is_nothing is True
    assert isinstance(result, Maybe)
    assert result.is_nothing
