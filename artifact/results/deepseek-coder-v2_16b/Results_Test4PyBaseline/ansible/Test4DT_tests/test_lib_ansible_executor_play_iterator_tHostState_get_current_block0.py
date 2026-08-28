
# Module: ansible.executor.play_iterator
import pytest
from ansible.executor.play_iterator import HostState, PlayIterator
import copy

# Test initialization with blocks
def test_host_state_initialization():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    assert isinstance(host_state, HostState)
    assert host_state._blocks == blocks
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

# Test copying the host state
def test_host_state_copy():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    new_host_state = host_state.copy()
    assert isinstance(new_host_state, HostState)
    assert new_host_state._blocks == blocks
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
    # Check that it's a deep copy by modifying the original and checking if the copy remains unchanged
    host_state._blocks[0]['regular'].append('new_task')
    with pytest.raises(AssertionError):  # Use raises to ensure assertion failure is detected
        assert 'new_task' not in new_host_state._blocks[0]['regular']

# Test accessing the current block's tasks
def test_get_current_block():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    current_block = host_state.get_current_block()
    assert current_block == blocks[0]
