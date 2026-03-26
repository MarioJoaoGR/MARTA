
import pytest
from pytutils.memo import CachedException

def test_valid_input():
    ex = ValueError('Example error')
    cached_exception = CachedException(ex)
    
    with pytest.raises(ValueError) as exc_info:
        cached_exception.throw()
        
    assert str(exc_info.value) == 'Example error'
