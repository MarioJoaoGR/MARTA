
# Module: ansible.playbook.block
# test_block.py
from ansible.playbook.block import Block

def test_get_dep_chain_no_parent():
    block = Block()
    assert block.get_dep_chain() is None, "Expected get_dep_chain to return None when no parent"

def test_get_dep_chain_single_level_inheritance():
    parent_block = Block()
    child_block = Block(parent_block=parent_block)
    assert child_block.get_dep_chain() == parent_block.get_dep_chain(), "Expected get_dep_chain to return the same as parent's dep_chain"

def test_get_dep_chain_multi_level_inheritance():
    grandparent_block = Block()
    parent_block = Block(parent_block=grandparent_block)
    child_block = Block(parent_block=parent_block)
    assert child_block.get_dep_chain() == grandparent_block.get_dep_chain(), "Expected get_dep_chain to return the same as grandparent's dep_chain"

def test_get_dep_chain_no_inheritance():
    block = Block()
    assert block._dep_chain is None, "Expected _dep_chain to be None initially"
    chain = block.get_dep_chain()
    assert chain is None, "Expected get_dep_chain to return None if _dep_chain is not set"
