
import pytest
from ansible.playbook.block import Block

# Test setting loader for a new block without parent or role
def test_set_loader_without_parent_or_role():
    block = Block()
    my_loader = "some_loader"
    block.set_loader(my_loader)
    assert block._loader == my_loader

# Test setting loader for a block with parent
def test_set_loader_with_parent():
    parent_block = Block()
    child_block = Block(parent_block=parent_block)
    my_loader = "some_loader"
    child_block.set_loader(my_loader)
    assert child_block._loader == my_loader
    assert parent_block._loader == my_loader

# Test setting loader for a block with role