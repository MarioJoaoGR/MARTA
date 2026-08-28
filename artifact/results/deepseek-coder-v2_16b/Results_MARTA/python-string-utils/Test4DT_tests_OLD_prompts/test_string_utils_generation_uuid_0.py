
import pytest
from unittest.mock import patch
from string_utils.generation import uuid

# Test valid UUID generation without hex format
def test_valid_uuid():
    with patch('string_utils.generation.uuid4', return_value='97e3a716-6b33-4ab9-9bb1-8128cb24d76b'):
        assert uuid() == '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'

# Test valid UUID generation with hex format

# Test invalid input: None should raise TypeError