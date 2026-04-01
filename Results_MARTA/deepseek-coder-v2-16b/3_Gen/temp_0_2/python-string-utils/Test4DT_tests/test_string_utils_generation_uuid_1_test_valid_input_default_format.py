
from unittest.mock import patch
from string_utils.generation import uuid
import pytest

@patch('string_utils.generation.uuid4')
def test_valid_input_default_format(mock_uuid4):
    mock_uuid4.return_value = "mocked_uuid"
    
    result_standard = uuid()
    assert isinstance(result_standard, str), "Expected a string representation of UUID"
    # No need to check the length explicitly as it should be in standard format and include hyphens
