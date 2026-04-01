
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    try_instance = Try(None, False)
    assert not try_instance.is_success
    assert try_instance.value is None
