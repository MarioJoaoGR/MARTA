
import pytest
from pymonet.monad_try import Try
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value='Hello', is_nothing=False)
    try_instance = maybe.to_try()
    
    assert isinstance(try_instance, Try)
    assert try_instance.is_success == True
    assert try_instance.value == 'Hello'
