
import pytest
from pymonet.monad_try import Try
from pymonet.maybe import Maybe

def test_edge_case():
    # Test with None value
    maybe_none = Maybe(value=None, is_nothing=True)
    try_none = maybe_none.to_try()
    assert isinstance(try_none, Try)
    assert not try_none.is_success
    assert try_none.value is None

    # Test with True/False boundary values
    maybe_true = Maybe(value='test', is_nothing=False)
    try_true = maybe_true.to_try()
    assert isinstance(try_true, Try)
    assert try_true.is_success
    assert try_true.value == 'test'

    # Test with True/False boundary values
    maybe_false = Maybe(value='test', is_nothing=False)
    try_false = maybe_false.to_try()
    assert isinstance(try_false, Try)
    assert try_false.is_success
    assert try_false.value == 'test'
