
# Module: string_utils.generation
# test_string_utils.py
from unittest.mock import patch
import pytest
from uuid import uuid4
from string_utils import uuid

@patch('uuid.uuid4')
def test_uuid_default(mock_uuid):
    mock_uuid.return_value = "97e3a716-6b33-4ab9-9bb1-8128cb24d76b"
    assert isinstance(uuid(), str) and len(uuid()) == 36, f"Expected a standard UUID string but got: {uuid()}"

@patch('uuid.uuid4')
def test_uuid_hex(mock_uuid):
    mock_uuid.return_value = "97e3a716-6b33-4ab9-9bb1-8128cb24d76b"