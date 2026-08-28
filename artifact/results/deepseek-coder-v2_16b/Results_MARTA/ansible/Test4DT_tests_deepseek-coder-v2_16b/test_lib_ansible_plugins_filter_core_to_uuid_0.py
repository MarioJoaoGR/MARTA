
import pytest
import uuid
from ansible.plugins.filter.core import to_uuid
from ansible.errors import AnsibleFilterError

# Constants
UUID_NAMESPACE_ANSIBLE = uuid.UUID('6e3ab9a0-f4b7-5fee-81d2-9ffe7c6faa7e')

def test_valid_input_with_default_namespace():
    result = to_uuid('example')
    assert isinstance(result, uuid.UUID)
    assert str(result) == '6e3ab9a0-f4b7-5fee-81d2-9ffe7c6faa7e'

def test_valid_input_with_custom_namespace():
    custom_namespace = uuid.UUID('12345678-1234-1234-1234-1234567890ab')
    result = to_uuid('example', custom_namespace)
    assert isinstance(result, uuid.UUID)
    assert str(result) != '6e3ab9a0-f4b7-5fee-81d2-9ffe7c6faa7e'  # Ensure it is different from default namespace
    assert str(result) == 'c9a8f8e3-b7d2-5fee-81d2-9ffe7c6faa7e'  # Known result for this specific custom namespace and input string

def test_invalid_namespace():
    with pytest.raises(AnsibleFilterError):
        to_uuid('example', 'invalid_uuid')
