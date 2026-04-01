
import pytest
from pymonet.validation import Validation

class Right:
    """Not successfully Either"""
    def __init__(self):
        self.value = None

    def to_validation(self):
        """
        Transform Either into Validation.

        :returns: successfull Validation monad with previous value
        :rtype: Validation[A, []]
        """
        from pymonet.validation import Validation

        return Validation.success(self.value)

def test_edge_case_none():
    right_instance = Right()
    right_instance.value = None
    
    validation_monad = right_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success() is True
    assert validation_monad.value is None
