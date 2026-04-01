
import pytest
from unittest.mock import patch
from flutes.multiproc import DummyApplyResult

def test_valid_input():
    # Arrange
    value = 42
    
    # Act
    result = DummyApplyResult(value)
    
    # Assert
    assert isinstance(result, DummyApplyResult)
    assert result._value == value
