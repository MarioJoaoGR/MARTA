
import pytest
from ansible.executor.play_iterator import HostState
import copy

# Test initialization with blocks
def test_host_state_initialization():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    
    assert host_state._blocks == blocks
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 0
    assert host_state.cur_always_task == 0

# Test the __repr__ method to ensure it returns a string representation of the HostState object
def test_host_state_repr():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    
    expected_repr = "HostState(%r)" % blocks
    assert repr(host_state) == expected_repr

# Test the copy method to ensure it creates a deep copy of the HostState object
def test_host_state_copy():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    copied_host_state = host_state.copy()
    
    # Check that the original and copied objects are not the same instance
    assert host_state is not copied_host_state
    # Check that the contents of the original and copied objects are identical
    assert host_state._blocks == copied_host_state._blocks
    assert host_state.cur_block == copied_host_state.cur_block
    assert host_state.cur_regular_task == copied_host_state.cur_regular_task
    assert host_state.cur_rescue_task == copied_host_state.cur_rescue_task
    assert host_state.cur_always_task == copied_host_state.cur_always_task

# Test the get_current_block method to ensure it returns the expected tasks for the current block
def test_get_current_block():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    
    expected_current_block = blocks[0]  # The first block is expected to be returned
    assert host_state.get_current_block() == expected_current_block
