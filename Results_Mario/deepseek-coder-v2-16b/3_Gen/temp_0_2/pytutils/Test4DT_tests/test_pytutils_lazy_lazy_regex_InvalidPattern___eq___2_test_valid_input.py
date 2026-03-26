
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_input():
    # Arrange
    msg = "This is a valid message"
    
    # Act
    instance = InvalidPattern(msg)
    
    # Assert
    assert isinstance(instance, InvalidPattern), "Instance should be an instance of InvalidPattern"
    assert instance.msg == msg, f"Expected msg to be '{msg}', but got '{instance.msg}'"
