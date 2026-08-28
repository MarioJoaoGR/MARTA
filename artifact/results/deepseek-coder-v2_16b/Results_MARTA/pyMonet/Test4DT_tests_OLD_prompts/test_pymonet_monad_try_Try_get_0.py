
import pytest
from pymonet.monad_try import Try

# Test valid input scenario
def test_get_valid_value():
    try_object = Try(42, True)
    assert try_object.get() == 42

# Test invalid input scenario where is_success is False