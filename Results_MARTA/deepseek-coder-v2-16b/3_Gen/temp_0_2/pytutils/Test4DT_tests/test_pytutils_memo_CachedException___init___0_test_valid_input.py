
import pytest
from pytutils.memo import CachedException

def test_valid_input():
    ex = ValueError("Invalid value")
    exception_instance = CachedException(ex)
    assert isinstance(exception_instance, CachedException)
    assert exception_instance.ex == ex
