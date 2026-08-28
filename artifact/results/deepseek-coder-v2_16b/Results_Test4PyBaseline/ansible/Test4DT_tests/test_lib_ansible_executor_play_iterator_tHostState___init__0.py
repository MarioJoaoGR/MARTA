
import pytest
from ansible.executor.play_iterator import HostState, PlayIterator
import copy

# Test initialization with basic blocks
def test_host_state_initialization_basic():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    
    assert len(host_state._blocks) == 2
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 0
    assert host_state.cur_always_task == 0
    assert host_state.run_state == PlayIterator.ITERATING_SETUP
    assert host_state.fail_state == PlayIterator.FAILED_NONE
    assert not host_state.pending_setup
    assert host_state.tasks_child_state is None
    assert host_state.rescue_child_state is None
    assert host_state.always_child_state is None
    assert not host_state.did_rescue
    assert not host_state.did_start_at_task

# Test initialization with specific blocks
def test_host_state_initialization_specific():
    blocks = [
        {'regular': [], 'rescue': ['rescue_task1'], 'always': []},
        {'regular': ['regular_task1'], 'rescue': [], 'always': ['always_task1']}
    ]
    host_state = HostState(blocks)
    
    assert len(host_state._blocks) == 2
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 1
    assert host_state.cur_always_task == 1
    assert host_state.run_state == PlayIterator.ITERATING_SETUP
    assert host_state.fail_state == PlayIterator.FAILED_NONE
    assert not host_state.pending_setup
    assert host_state.tasks_child_state is None
    assert host_state.rescue_child_state is None
    assert host_state.always_child_state is None
    assert not host_state.did_rescue
    assert not host_state.did_start_at_task

# Test initialization with empty blocks
def test_host_state_initialization_empty():
    blocks = [
        {'regular': [], 'rescue': [], 'always': []},
        {'regular': [], 'rescue': [], 'always': []}
    ]
    host_state = HostState(blocks)
    
    assert len(host_state._blocks) == 2
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 0
    assert host_state.cur_always_task == 0
    assert host_state.run_state == PlayIterator.ITERATING_SETUP
    assert host_state.fail_state == PlayIterator.FAILED_NONE
    assert not host_state.pending_setup
    assert host_state.tasks_child_state is None
    assert host_state.rescue_child_state is None
    assert host_state.always_child_state is None
    assert not host_state.did_rescue
    assert not host_state.did_start_at_task

# Test copy method
def test_host_state_copy():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    
    new_host_state = host_state.copy()
    
    assert len(new_host_state._blocks) == 2
    assert new_host_state.cur_block == 0
    assert new_host_state.cur_regular_task == 0
    assert new_host_state.cur_rescue_task == 0
    assert new_host_state.cur_always_task == 0
    assert new_host_state.run_state == PlayIterator.ITERATING_SETUP
    assert new_host_state.fail_state == PlayIterator.FAILED_NONE
    assert not new_host_state.pending_setup
    assert new_host_state.tasks_child_state is None
    assert new_host_state.rescue_child_state is None
    assert new_host_state.always_child_state is None
    assert not new_host_state.did_rescue
    assert not new_host_state.did_start_at_task
