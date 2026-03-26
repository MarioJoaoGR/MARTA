
import pytest
from flutes.iterator import chunk

def test_error_case_invalid_n():
    n = 0
    iterable = range(10)
    
    with pytest.raises(ValueError, match="`n` should be positive"):
        list(chunk(n, iterable))
