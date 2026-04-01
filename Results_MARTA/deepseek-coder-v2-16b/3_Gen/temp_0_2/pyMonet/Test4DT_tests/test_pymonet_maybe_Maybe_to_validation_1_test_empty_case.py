
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_empty_case():
    maybe_instance = Maybe(None, True)
    validation_monad = maybe_instance.to_validation()
    
    assert isinstance(validation_monad, Validation)
    assert validation_monad.value is None
    assert validation_monad.errors == []
