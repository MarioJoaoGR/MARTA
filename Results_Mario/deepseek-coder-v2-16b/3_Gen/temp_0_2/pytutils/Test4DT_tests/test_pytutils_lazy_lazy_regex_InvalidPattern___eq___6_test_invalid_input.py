
from unittest.mock import Mock
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_input():
    # Arrange
    msg = "The provided pattern does not match any expected format."
    invalid_pattern = InvalidPattern(msg)
    
    # Act and Assert
    assert invalid_pattern.msg == msg
