
from pymonet.validation import Validation

def test_valid_inputs():
    # Create a successful Validation instance
    success_val = Validation.success(50)
    
    # Check that the value is correct and there are no errors
    assert success_val.value == 50
    assert len(success_val.errors) == 0
