
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    error_try_object = Try(None, False)
    mapped_error_try_object = error_try_object.map(lambda x: x ** 2)
    
    assert not mapped_error_try_object.is_success
    assert mapped_error_try_object.value is None
