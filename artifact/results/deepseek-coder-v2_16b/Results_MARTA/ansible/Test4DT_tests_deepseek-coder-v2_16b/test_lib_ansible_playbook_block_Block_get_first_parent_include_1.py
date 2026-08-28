
import pytest
from ansible.playbook.block import Block


def test_no_parent():
    block = Block()
    first_include = block.get_first_parent_include()
    assert first_include is None, "Expected no parent include if there's no parent set"