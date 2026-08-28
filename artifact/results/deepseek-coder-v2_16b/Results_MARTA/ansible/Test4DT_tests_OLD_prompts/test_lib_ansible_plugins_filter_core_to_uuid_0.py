
import pytest
from unittest.mock import patch
import uuid
from ansible.plugins.filter.core import UUID_NAMESPACE_ANSIBLE, to_uuid, AnsibleFilterError



def test_invalid_namespace():
    with pytest.raises(AnsibleFilterError):
        to_uuid('example', 'invalid-namespace')