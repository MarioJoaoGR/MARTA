
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_input():
    # Arrange
    msg = "This is a valid message."
    
    # Act & Assert
    try:
        raise InvalidPattern(msg)
    except InvalidPattern as e:
        assert e.msg == msg
