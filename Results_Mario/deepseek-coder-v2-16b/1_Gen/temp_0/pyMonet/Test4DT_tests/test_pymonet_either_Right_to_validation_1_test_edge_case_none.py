
from pymonet.either import Right
from pymonet.validation import Validation
import pytest

def test_edge_case_none():
    # Create a Right instance with a value of None
    right_instance = Right(None)
    
    # Call the to_validation method on the Right instance
    validation_monad = right_instance.to_validation()
    
    # Assert that the resulting Validation monad is successful and contains the original value (None)
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value is None
