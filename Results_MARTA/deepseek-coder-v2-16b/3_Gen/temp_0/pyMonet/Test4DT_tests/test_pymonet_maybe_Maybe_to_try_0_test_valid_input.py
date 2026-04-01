
import pytest
from pymonet.monad_try import Try
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    result = maybe.to_try()
    assert isinstance(result, Try)
    assert result.is_success
    assert result.value == 42
