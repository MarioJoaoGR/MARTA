
import pytest
from pymonet.monad_try import Try
from pymonet.box import Box

def test_edge_case():
    box = Box(None)
    try_monad = box.to_try()
    assert isinstance(try_monad, Try)
    assert try_monad.is_success is True
    assert try_monad.value is None
