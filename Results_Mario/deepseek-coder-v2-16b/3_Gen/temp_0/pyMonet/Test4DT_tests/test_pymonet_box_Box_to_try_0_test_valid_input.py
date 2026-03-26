
import pytest
from pymonet.box import Box

def test_valid_input():
    box = Box(42)
    try_monad = box.to_try()
    
    assert try_monad.is_success is True
    assert try_monad.value == 42
