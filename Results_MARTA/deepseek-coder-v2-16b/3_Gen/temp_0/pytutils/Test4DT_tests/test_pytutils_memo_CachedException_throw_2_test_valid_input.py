
import pytest
from pytutils.memo import CachedException

class CustomError(Exception):
    pass

def test_valid_input():
    cached_exception = CachedException(CustomError('An error occurred'))
    with pytest.raises(CustomError) as exc_info:
        cached_exception.throw()
    assert str(exc_info.value) == 'An error occurred'
