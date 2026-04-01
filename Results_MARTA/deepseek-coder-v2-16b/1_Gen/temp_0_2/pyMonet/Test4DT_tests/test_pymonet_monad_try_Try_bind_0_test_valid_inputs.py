
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    def example_function(x):
        return Try(x + "!", True)
    
    success = Try("example", True)
    assert success.bind(example_function).value == "example!"
