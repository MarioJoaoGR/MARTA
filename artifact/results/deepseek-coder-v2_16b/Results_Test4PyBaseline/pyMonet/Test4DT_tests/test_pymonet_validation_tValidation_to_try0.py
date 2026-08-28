
import pytest
from pymonet.validation import Validation
from pymonet.monad_try import Try

# Test successful Validation to Try conversion
def test_successful_to_try():
    val = Validation(10, [])
    try_instance = val.to_try()
    assert isinstance(try_instance, Try)