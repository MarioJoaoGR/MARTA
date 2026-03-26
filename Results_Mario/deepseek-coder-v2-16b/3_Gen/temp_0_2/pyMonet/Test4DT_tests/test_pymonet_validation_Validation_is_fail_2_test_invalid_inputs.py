
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test with a valid value and no errors
    validation = Validation(value=10, errors=[])
    assert not validation.is_fail()
    
    # Test with an invalid value and some errors
    validation = Validation(value=None, errors=['Error1', 'Error2'])
    assert validation.is_fail()
    
    # Test with a valid value but with accumulated errors
    validation = Validation(value=10, errors=['Error3'])
    assert validation.is_fail()  # Adding another error should make it fail
