
import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

# Test initialization with default parameters
def test_init_default():
    block = Block()
    assert hasattr(block, '_play') and block._play is None