
import pytest
from pymonet.either import Left, Right

def test_valid_input():
    left_instance = Left("error message")
    monad_with_function = Left(lambda x: x * 2)
    
    result = left_instance.ap(monad_with_function)
    
    assert isinstance(result, Left)
    assert result.value == "error message"
