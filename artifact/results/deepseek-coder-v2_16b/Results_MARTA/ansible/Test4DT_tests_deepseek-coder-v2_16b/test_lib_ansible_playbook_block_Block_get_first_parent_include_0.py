
import pytest
from ansible.playbook.block import Block

def test_invalid_input():
    # Instantiate the Block with an invalid parent block (a string)
    block = Block(parent_block='invalid')
    
    # Call the method to retrieve the first parent include
    with pytest.raises(AttributeError):
        result = block.get_first_parent_include()
