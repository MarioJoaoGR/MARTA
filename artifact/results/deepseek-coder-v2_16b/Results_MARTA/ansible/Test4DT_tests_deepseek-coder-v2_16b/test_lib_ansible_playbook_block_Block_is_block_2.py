
import pytest
from ansible.playbook.block import Block


def test_is_block_with_valid_dict():
    # Test with a dictionary that contains 'block', 'rescue', or 'always' keys
    valid_dict = {'block': [], 'rescue': [], 'always': []}
    assert Block.is_block(valid_dict), "Expected is_block to return True for a dictionary containing 'block', 'rescue', or 'always'"

def test_is_block_with_invalid_dict():
    # Test with a dictionary that does not contain any of the keys 'block', 'rescue', or 'always'
    invalid_dict = {'foo': 'bar'}
    assert not Block.is_block(invalid_dict), "Expected is_block to return False for a dictionary without 'block', 'rescue', or 'always'"