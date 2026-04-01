
import pytest
from pymonet.box import Box

def test_edge_case():
    # Test with None input
    box = Box(None)
    
    # Call the method under test
    validation_monad = box.to_validation()
    
    # Assert that the conversion resulted in a successful Validation monad
    assert validation_monad.is_success(), "Expected success, but got failure"
    
    # Assert that the value within the Validation monad is None
    assert validation_monad.value is None, "Expected value to be None"
