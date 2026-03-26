
import pytest
from unittest.mock import patch
from flutes.multiproc import DummyApplyResult

def test_valid_input():
    # Arrange
    expected_value = 'some_result'
    
    # Act
    result = DummyApplyResult(value=expected_value)
    
    # Assert
    assert result._value == expected_value
