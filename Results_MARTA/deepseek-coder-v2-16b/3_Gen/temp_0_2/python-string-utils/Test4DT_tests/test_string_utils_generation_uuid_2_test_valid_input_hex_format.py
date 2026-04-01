
import pytest
from unittest.mock import patch
import uuid as py_uuid
from string_utils.generation import uuid

@patch('string_utils.generation.uuid4', return_value=py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b'))
def test_valid_input_hex_format(mock_uuid):
    assert uuid(as_hex=True) == '97e3a7166b334ab99bb18128cb24d76b'
