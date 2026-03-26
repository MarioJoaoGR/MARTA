
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    success_try = Try(10, True)
    assert success_try.is_success is True
    assert success_try.get() == 10
