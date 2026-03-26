# Module: string_utils.generation
import pytest
from unittest.mock import patch
import uuid as py_uuid

# Import the function from its module
from string_utils.generation import uuid

def test_default_behavior():
    with patch('string_utils.generation.uuid4', return_value=py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        result = uuid()
        assert isinstance(result, str), "Default behavior should return a string"
        assert len(result) == 36, "Default UUID should be in standard format with length 36"

def test_hex_behavior():
    with patch('string_utils.generation.uuid4', return_value=py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        result = uuid(as_hex=True)
        assert isinstance(result, str), "Hexadecimal behavior should return a string"
        assert len(result) == 32, "Hexadecimal UUID should be in hexadecimal format with length 32"

def test_default_behavior_assertion():
    with patch('string_utils.generation.uuid4', return_value=py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        result = uuid()
        assert isinstance(result, str), "Default behavior should return a string"
        assert len(result) == 36, "Default UUID should be in standard format with length 36"

def test_hex_behavior_assertion():
    with patch('string_utils.generation.uuid4', return_value=py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        result = uuid(as_hex=True)
        assert isinstance(result, str), "Hexadecimal behavior should return a string"
        assert len(result) == 32, "Hexadecimal UUID should be in hexadecimal format with length 32"
