
import pytest
from ansible.errors import AnsibleParserError
from lib.ansible.playbook.role_include import IncludeRole

def test_invalid_inputs():
    with pytest.raises(AnsibleParserError):
        # Test case where 'name' is not provided
        data = {'block': 'example', 'role': 'example_role'}
        IncludeRole.load(data=data)
