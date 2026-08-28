
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
    
    assert host_state._blocks == blocks, f"Expected {blocks}, but got {host_state._blocks}"
    assert host_state.cur_block == 0, f"Expected cur_block to be 0, but got {host_state.cur_block}"
    assert host_state.cur_regular_task == 0, f"Expected cur_regular_task to be 0, but got {host_state.cur_regular_task}"
    assert host_state.cur_rescue_task == 0, f"Expected cur_rescue_task to be 0, but got {host_state.cur_rescue_task}"
    assert host_state.cur_always_task == 0, f"Expected cur_always_task to be 0, but got {host_state.cur_always_task}"

# Test copying the host state
def test_host_state_copy():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    copied_host_state = copy.deepcopy(host_state)
    
    assert host_state._blocks == copied_host_state._blocks, f"Expected {host_state._blocks}, but got {copied_host_state._blocks}"
    assert host_state.cur_block == copied_host_state.cur_block, f"Expected cur_block to be {host_state.cur_block}, but got {copied_host_state.cur_block}"
    assert host_state.cur_regular_task == copied_host_state.cur_regular_task, f"Expected cur_regular_task to be {host_state.cur_regular_task}, but got {copied_host_state.cur_regular_task}"
    assert host_state.cur_rescue_task == copied_host_state.cur_rescue_task, f"Expected cur_rescue_task to be {host_state.cur_rescue_task}, but got {copied_host_state.cur_rescue_task}"
    assert host_state.cur_always_task == copied_host_state.cur_always_task, f"Expected cur_always_task to be {host_state.cur_always_task}, but got {copied_host_state.cur_always_task}"

# Test string representation of HostState
def test_host_state_str():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    
    expected_str = "HostState(%r)" % blocks