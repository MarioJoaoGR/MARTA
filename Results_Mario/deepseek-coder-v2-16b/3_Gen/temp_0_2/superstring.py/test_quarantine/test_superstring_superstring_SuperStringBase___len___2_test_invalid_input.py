
import pytest
from unittest.mock import patch
from superstring.superstring import SuperStringBase

class InvalidString(SuperStringBase):
    def __init__(self, value):
        super().__init__()
    
    def length(self):
        if not isinstance(self.value, str):
            raise ValueError('Input must be a string')

def test_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        invalid_instance = InvalidString(12345)  # Passing an integer instead of a string
    
    assert str(exc_info.value) == 'Input must be a string'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___len___2_test_invalid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___len___2_test_invalid_input.py:11:26: E1101: Instance of 'InvalidString' has no 'value' member (no-member)


"""