
import pytest
from ansible.playbook.block import Block

# Test cases for the __init__ method of the Block class
def test_block_initialization():
    # Test with only play specified
    block = Block(play={'name': 'example_play'})
    assert hasattr(block, '_play') and block._play == {'name': 'example_play'}