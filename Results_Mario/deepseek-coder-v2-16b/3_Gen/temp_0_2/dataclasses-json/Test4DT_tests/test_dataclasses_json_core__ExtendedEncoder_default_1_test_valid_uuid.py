
import pytest
from uuid import UUID
from dataclasses_json.core import _ExtendedEncoder
import json

@pytest.fixture
def encoder():
    return _ExtendedEncoder()

@pytest.mark.parametrize("uuid_obj, expected", [
    (UUID('123e4567-e89b-12d3-a456-426614174000'), '123e4567-e89b-12d3-a456-426614174000')
])
def test_valid_uuid(encoder, uuid_obj, expected):
    assert encoder.default(uuid_obj) == expected
