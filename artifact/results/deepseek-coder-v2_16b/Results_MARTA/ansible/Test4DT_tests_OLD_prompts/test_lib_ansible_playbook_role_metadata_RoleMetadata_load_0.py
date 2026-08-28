
import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata

def test_valid_metadata():
    role_data = {
        "name": "example-role",
        "version": "1.0.0",
        # other metadata fields...
    }
    with pytest.raises(AnsibleParserError):
        RoleMetadata.load(data=role_data, owner='example_owner')
