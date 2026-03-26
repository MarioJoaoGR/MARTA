
import pytest
from pymonet.validation import Validation

class Right:
    """Not successfully Either"""
    def __init__(self, value=None):
        self.value = value

    def to_validation(self):
        """
        Transform Either into Validation.

        :returns: successfull Validation monad with previous value
        :rtype: Validation[A, []]
        """
        from pymonet.validation import Validation

        return Validation.success(self.value)

def test_valid_input():
    right_instance = Right('valid_data')
    validation_monad = right_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success() is True
    assert validation_monad.value == 'valid_data'
