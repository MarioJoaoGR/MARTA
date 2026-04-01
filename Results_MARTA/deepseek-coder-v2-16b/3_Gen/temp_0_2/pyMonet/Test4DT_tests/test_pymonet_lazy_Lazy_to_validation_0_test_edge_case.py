
import pytest
from pymonet.lazy import Lazy
from pymonet.validation import Validation

def test_Lazy_to_validation():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    
    # Test the to_validation method
    validation_monad = lazy.to_validation(5)
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value == 25
