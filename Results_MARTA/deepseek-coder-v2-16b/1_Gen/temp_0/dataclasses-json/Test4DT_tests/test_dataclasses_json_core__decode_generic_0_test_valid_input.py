
import pytest
from dataclasses import dataclass, fields
from typing import Optional, Union
from dataclasses_json.core import _decode_generic
from unittest.mock import patch, MagicMock

# Define a mock dataclass for testing
@dataclass
class MockX:
    field1: int
    field2: str

# Test cases for _decode_generic function
def test_valid_input():
    with patch('dataclasses_json.core._is_collection') as mock_is_collection, \
         patch('dataclasses_json.core._is_mapping') as mock_is_mapping, \
         patch('dataclasses_json.core._is_tuple') as mock_is_tuple, \
         patch('dataclasses_json.core._is_counter') as mock_is_counter:

        # Mock the return values for the type checks
        mock_is_collection.return_value = False
        mock_is_mapping.return_value = False
        mock_is_tuple.return_value = False
        mock_is_counter.return_value = False

        # Define a dictionary to be used as JSON data
        json_data = {'field1': 42, 'field2': 'test'}

        # Call the function with valid input
        result = _decode_generic(MockX, json_data, infer_missing=False)

        # Assert that the result is an instance of MockX and has the correct values
        assert isinstance(result, MockX)
        assert result.field1 == 42
        assert result.field2 == 'test'

if __name__ == "__main__":
    pytest.main()
