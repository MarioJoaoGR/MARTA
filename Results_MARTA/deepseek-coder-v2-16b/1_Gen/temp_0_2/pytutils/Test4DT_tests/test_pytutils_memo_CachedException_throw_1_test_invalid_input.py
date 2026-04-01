
import pytest
from pytutils.memo import CachedException

def test_invalid_input():
    ex = 'NotAnException'
    with pytest.raises(TypeError):
        cached_exception = CachedException(ex)
        cached_exception.throw()
