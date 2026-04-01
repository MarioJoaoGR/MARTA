
import pytest
from pymonet.either import Left, Right

def test_left_ap():
    left_instance = Left("error message")
    another_monad = Right(lambda x: x * 2)
    
    result = left_instance.ap(another_monad)
    
    assert isinstance(result, Left)
    assert result.value == "error message"
