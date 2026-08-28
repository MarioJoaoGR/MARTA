
# Module: ansible.playbook.block
# test_block.py
from ansible.playbook.block import Block

def test_get_include_params_no_parent():
    # Create a Block instance without a parent
    block = Block()
    
    # Test that get_include_params returns an empty dictionary when no parent is set
    assert block.get_include_params() == {}

def test_get_include_params_with_parent():
    # Create a mock parent block for testing
    class MockParentBlock:
        def get_include_params(self):
            return {'key': 'value'}
    
    # Create a Block instance with a mock parent
    block = Block()
    block._parent = MockParentBlock()
    
    # Test that get_include_params calls the parent's method and returns its result
    assert block.get_include_params() == {'key': 'value'}
