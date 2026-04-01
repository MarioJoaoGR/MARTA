
from unittest.mock import patch
import uuid as py_uuid
from string_utils.generation import uuid

def test_valid_input_default_format():
    with patch('string_utils.generation.uuid4', side_effect=lambda: py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        assert uuid() == '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'
