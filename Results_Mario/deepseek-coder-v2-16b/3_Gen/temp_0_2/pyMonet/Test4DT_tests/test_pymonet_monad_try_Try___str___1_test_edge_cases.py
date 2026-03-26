
import pytest
from pymonet.monad_try import Try  # Assuming this is a hypothetical module, adjust accordingly

def test_edge_cases():
    none_try = Try(None, True)
    empty_list_try = Try([], False)
    
    assert str(none_try) == 'Try[value=None, is_success=True]'
    assert none_try.is_success is True
    assert none_try.value is None
    
    assert str(empty_list_try) == 'Try[value=[], is_success=False]'
    assert empty_list_try.is_success is False
    assert len(empty_list_try.value) == 0
