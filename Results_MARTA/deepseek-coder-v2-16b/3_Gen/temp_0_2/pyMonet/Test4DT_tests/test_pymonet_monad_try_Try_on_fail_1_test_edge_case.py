
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    error_try_instance = Try(None, False)
    assert not error_try_instance.is_success
    assert error_try_instance.value is None
    
    def print_error(value):
        assert value is None
    
    error_try_instance.on_fail(print_error)
