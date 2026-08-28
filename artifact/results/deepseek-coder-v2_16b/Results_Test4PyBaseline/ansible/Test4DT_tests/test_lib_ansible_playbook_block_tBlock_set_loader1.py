
import pytest
from ansible.playbook.block import Block

# Test case 8: Setting the loader for a Block instance
def test_set_loader():
    block = Block()
    loader = "my_loader"
    block.set_loader(loader)
    assert block._loader == loader, f"Expected _loader to be {loader}, but got {block._loader}"

# Test case 9: Setting the loader for a Block instance with a parent
def test_set_loader_with_parent():
    parent_block = Block()
    child_block = Block(parent_block=parent_block)
    loader = "my_loader"
    parent_block.set_loader(loader)
    assert parent_block._loader == loader, f"Expected parent block _loader to be {loader}, but got {parent_block._loader}"