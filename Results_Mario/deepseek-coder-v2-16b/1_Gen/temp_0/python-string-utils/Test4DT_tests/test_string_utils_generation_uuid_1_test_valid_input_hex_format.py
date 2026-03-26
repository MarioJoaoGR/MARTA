
import pytest
from unittest.mock import patch
from uuid import UUID, uuid4
from string_utils.generation import uuid as gen_uuid

@pytest.mark.skip(reason="Need to fix the test case")
def test_valid_input_hex_format():
    with patch('string_utils.generation.uuid', side_effect=lambda: UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        assert gen_uuid(as_hex=True) == '97e3a7166b334ab99bb18128cb24d76b'
