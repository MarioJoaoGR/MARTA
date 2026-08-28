
import pytest
import uuid
from unittest.mock import patch
from typesystem.formats import UUIDFormat

def test_valid_uuid():
    with patch('typesystem.formats.UUIDFormat.is_native_type', return_value=True):
        uuid_format = UUIDFormat()
        valid_uuid = "123e4567-e89b-12d3-a456-426614174000"
        assert uuid_format.is_native_type(valid_uuid) is True

def test_invalid_uuid():
    with patch('typesystem.formats.UUIDFormat.is_native_type', return_value=False):
        uuid_format = UUIDFormat()
        invalid_uuid = "not-a-valid-uuid"
        assert uuid_format.is_native_type(invalid_uuid) is False

def test_none_input():
    with patch('typesystem.formats.UUIDFormat.is_native_type', side_effect=TypeError):
        uuid_format = UUIDFormat()
        with pytest.raises(TypeError):
            uuid_format.is_native_type(None)
