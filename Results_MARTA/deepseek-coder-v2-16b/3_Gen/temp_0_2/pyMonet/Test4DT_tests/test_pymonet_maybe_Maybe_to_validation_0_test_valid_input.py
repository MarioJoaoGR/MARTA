
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_valid_input():
    maybe_instance = Maybe(42, False)
    validation_monad = maybe_instance.to_validation()
    
    assert isinstance(validation_monad, Validation)
    assert validation_monad.value == 42
    assert validation_monad.errors == []
