
import pytest
from pymonet.monad_try import Try

def test_missing_arguments():
    with pytest.raises(TypeError):
        Try()  # Missing arguments should raise TypeError

def test_missing_is_success():
    with pytest.raises(TypeError):
        Try(None)  # Missing is_success argument should raise TypeError

def test_valid_instance():
    try_none = Try(None, True)  # None as value and success
    assert try_none.value is None
    assert try_none.is_success is True
