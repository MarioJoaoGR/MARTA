
# Module: ansible.playbook.block
# test_block.py
from ansible.playbook.block import Block

def test_block_initialization():
    # Test creating a Block instance without any specific tasks or handlers
    block1 = Block()
    assert hasattr(block1, '_play'), "Block should have an attribute _play"