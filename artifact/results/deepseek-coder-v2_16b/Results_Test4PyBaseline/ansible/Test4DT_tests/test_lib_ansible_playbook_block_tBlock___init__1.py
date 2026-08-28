
# Module: ansible.playbook.block
# test_block.py
from ansible.playbook.block import Block

def test_block_with_task_include():
    play = {'name': 'example_play'}
    task_include = {'action': 'run'}
    block = Block(play=play, role='admin', task_include=task_include)
    assert block._play == play
    assert block._role == 'admin'
    assert block._parent == task_include
    assert not block._use_handlers
    assert not block._implicit

def test_block_with_parent_block():
    parent_block = Block(play={'name': 'parent_play'})
    block = Block(parent_block=parent_block)
    assert block._play is None
    assert block._role is None
    assert block._parent == parent_block
    assert not block._use_handlers
    assert not block._implicit

def test_block_without_configuration():
    block = Block()
    assert block._play is None
    assert block._role is None
    assert block._parent is None
    assert not block._use_handlers
    assert not block._implicit

def test_block_with_use_of_handlers():
    block = Block(use_handlers=True)
    assert block._play is None
    assert block._role is None
    assert block._parent is None
    assert block._use_handlers
    assert not block._implicit

def test_block_with_implicit_configuration():
    block = Block(implicit=True)
    assert block._play is None
    assert block._role is None
    assert block._parent is None
    assert not block._use_handlers
    assert block._implicit
