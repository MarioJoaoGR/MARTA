
import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError



def test_invalid_input():
    with pytest.raises(TypeError):
        Block(invalid_param='invalid')  # Invalid parameter to trigger an error