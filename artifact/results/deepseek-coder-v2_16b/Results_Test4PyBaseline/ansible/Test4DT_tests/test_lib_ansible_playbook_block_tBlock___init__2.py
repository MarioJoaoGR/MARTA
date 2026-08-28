
# Module: ansible.playbook.block
# test_block.py
from ansible.playbook.block import Block

def test_block_with_task_include():
    task_include = {'some': 'configuration'}
    block = Block(task_include=task_include)
    assert block._parent == task_include
    assert not block._use_handlers
    assert not block._implicit

def test_block_with_parent_block():
    parent_block = Block()
    block = Block(parent_block=parent_block)
    assert block._parent == parent_block
    assert not block._use_handlers
    assert not block._implicit

def test_block_with_role():
    role = 'example_role'
    block = Block(role=role)
    assert block._role == role
    assert not block._use_handlers
    assert not block._implicit

def test_block_without_configuration():
    block = Block()
    assert block._parent is None
    assert block._role is None
    assert not block._use_handlers
    assert not block._implicit

def test_block_with_use_of_handlers():
    use_handlers = True
    block = Block(use_handlers=use_handlers)
    assert not block._parent
    assert not block._role
    assert block._use_handlers
    assert not block._implicit

def test_block_with_implicit_configuration():
    implicit = True
    block = Block(implicit=implicit)
    assert not block._parent
    assert not block._role
    assert not block._use_handlers
    assert block._implicit
