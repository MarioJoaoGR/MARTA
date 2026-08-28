
import pytest
from ansible.playbook.block import Block


def test_get_include_params():
    # Test that get_include_params returns an empty dictionary when no parent is set
    block = Block()
    assert block.get_include_params() == {}
