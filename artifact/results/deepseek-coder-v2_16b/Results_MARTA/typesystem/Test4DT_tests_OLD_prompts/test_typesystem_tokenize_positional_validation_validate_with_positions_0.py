
import pytest
from unittest.mock import patch, MagicMock
from typesystem.tokenize.positional_validation import validate_with_positions, Token, Field, Schema, ValidationError, Message

# Test scenario 1: Validate a token with a valid validator
def test_validate_with_positions_valid():
    # Mock the Token and Validator classes
    mock_token = MagicMock()
    mock_validator = MagicMock()
    
    # Set up the mock to return a valid result for validation
    mock_validator.validate.return_value = True
    
    # Call the function under test
    with patch('typesystem.tokenize.positional_validation.ValidationError', side_effect=ValidationError):
        result = validate_with_positions(token=mock_token, validator=mock_validator)
        
        # Assert that the mock validator's validate method was called correctly
        assert result is True
        mock_validator.validate.assert_called_once_with(mock_token.value)

# Test scenario 2: Validate a token with an invalid validator, raising ValidationError

# Test scenario 3: Validate a token with required field error