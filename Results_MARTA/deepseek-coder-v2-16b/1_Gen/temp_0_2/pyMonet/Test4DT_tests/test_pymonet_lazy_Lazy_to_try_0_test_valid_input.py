
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    try_monad = lazy.to_try(5)
    
    assert try_monad.is_success, "Expected the Try monad to be successful"
    assert try_monad.value == 25, "Expected the value of square(5) to be 25"
