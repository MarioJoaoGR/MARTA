# Module: ansible.playbook.block
import pytest
from ansible.playbook.block import Block

# Test initialization with all parameters provided
def test_init_with_all_parameters():
    block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    assert block._play == {'name': 'example_play'}
    assert block._role == 'admin'
    assert block._parent == 'included_tasks'
    assert not block._use_handlers
    assert not block._implicit

# Test initialization without any parameters
def test_init_without_parameters():
    block = Block()
    assert block._play is None
    assert block._role is None
    assert block._parent is None
    assert not block._use_handlers
    assert not block._implicit

# Test copy method with default settings
def test_copy_default():
    original_block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    new_block = original_block.copy()
    assert isinstance(new_block, Block)
    assert new_block._play == {'name': 'example_play'}
    assert new_block._role == 'admin'
    assert new_block._parent == 'included_tasks'
    assert not new_block._use_handlers
    assert not new_block._implicit

# Test copy method with exclude_parent set to True
def test_copy_exclude_parent():
    original_block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    new_block = original_block.copy(exclude_parent=True)
    assert isinstance(new_block, Block)
    assert new_block._play == {'name': 'example_play'}
    assert new_block._role == 'admin'
    assert new_block._parent is None
    assert not new_block._use_handlers
    assert not new_block._implicit

# Test copy method with exclude_tasks set to True
def test_copy_exclude_tasks():
    original_block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    new_block = original_block.copy(exclude_tasks=True)
    assert isinstance(new_block, Block)
    assert new_block._play == {'name': 'example_play'}
    assert new_block._role == 'admin'
    assert new_block._parent == 'included_tasks'
    assert not new_block._use_handlers
    assert not new_block._implicit
    assert len(new_block.block) == 0
    assert len(new_block.rescue) == 0
    assert len(new_block.always) == 0

# Test copy method with both exclude_parent and exclude_tasks set to True
def test_copy_exclude_both():
    original_block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    new_block = original_block.copy(exclude_parent=True, exclude_tasks=True)
    assert isinstance(new_block, Block)
    assert new_block._play == {'name': 'example_play'}
    assert new_block._role == 'admin'
    assert new_block._parent is None
    assert not new_block._use_handlers
    assert not new_block._implicit
    assert len(new_block.block) == 0
    assert len(new_block.rescue) == 0
    assert len(new_block.always) == 0

# Test copy method with no changes (default behavior)
def test_copy_no_changes():
    original_block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    new_block = original_block.copy()
    assert isinstance(new_block, Block)
    assert new_block._play == {'name': 'example_play'}
    assert new_block._role == 'admin'
    assert new_block._parent == 'included_tasks'
    assert not new_block._use_handlers
    assert not new_block._implicit
