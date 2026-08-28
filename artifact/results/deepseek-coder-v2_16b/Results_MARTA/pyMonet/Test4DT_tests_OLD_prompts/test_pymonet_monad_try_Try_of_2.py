
import pytest
from unittest.mock import patch
from pymonet.monad_try import Try

def test_valid_input():
    def valid_function(x):
        return x + 1
    
    try_instance = Try.of(valid_function, 41)
    assert try_instance.is_success is True
    assert try_instance.value == 42

