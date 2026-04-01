
from pymonet.either import Right
from pymonet.validation import Validation
import pytest

def test_edge_case_none():
    # Create a Right instance with None value
    right_instance = Right(None)
    
    # Call the to_validation method
    validation_monad = right_instance.to_validation()
    
    # Assert that the resulting Validation monad is successful and contains the original value (None)
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value is None
