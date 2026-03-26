
from pymonet.maybe import Maybe

def test_valid_input():
    # Test when Maybe is not empty
    maybe = Maybe(value=42, is_nothing=False)
    assert maybe.is_nothing == False
    assert maybe.value == 42
    
    def mapper(x):
        return Maybe(value=x * 2, is_nothing=False)
    
    # Test bind method with a valid mapper function
    result = maybe.bind(mapper)
    assert isinstance(result, Maybe)
    assert not result.is_nothing
    assert result.value == 84
    
    # Test when Maybe is empty
    nothing = Maybe(value=None, is_nothing=True)
    assert nothing.is_nothing == True
    
    # Test bind method with an empty Maybe
    result_empty = nothing.bind(mapper)
    assert isinstance(result_empty, Maybe)
    assert result_empty.is_nothing
