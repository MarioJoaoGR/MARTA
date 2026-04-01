
from unittest.mock import patch
import uuid as uuid_module
import pytest
from string_utils.generation import uuid

@pytest.mark.parametrize("as_hex", [True, False])
def test_invalid_input_none(as_hex):
    with patch('string_utils.generation.uuid4', return_value=uuid_module.UUID('123e4567-e89b-12d3-a456-426614174000')):
        if as_hex:
            assert uuid(as_hex=True) == '123e4567e89b12d3a456426614174000'
        else:
            assert uuid() == '123e4567-e89b-12d3-a456-426614174000'
