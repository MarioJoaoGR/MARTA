
from pytutils.memo import CachedException
import pytest

def test_edge_case():
    ex = ValueError("Test error")
    cached_exception = CachedException(ex)
    with pytest.raises(ValueError):
        cached_exception.throw()
