
# Module: ansible.executor.play_iterator
import pytest
from ansible.executor.play_iterator import HostState
import copy

# Test initialization of HostState with different blocks
def test_host_state_initialization():
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
    assert host_state.run_state == 'ITERATING_SETUP'
    assert host_state.fail_state == 'FAILED_NONE'
    assert not host_state.pending_setup
    assert host_state.tasks_child_state is None
    assert host_state.rescue_child_state is None
    assert host_state.always_child_state is None
    assert not host_state.did_rescue
    assert not host_state.did_start_at_task

# Test copying of HostState
def test_host_state_copy():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    new_host_state = host_state.copy()
    assert isinstance(new_host_state, HostState)
    for attr in ('_blocks', 'cur_block', 'cur_regular_task', 'cur_rescue_task', 'cur_always_task',
                 'run_state', 'fail_state', 'pending_setup',
                 'tasks_child_state', 'rescue_child_state', 'always_child_state'):
        assert getattr(host_state, attr) == getattr(new_host_state, attr)

# Test equality of HostState instances
def test_host_state_equality():
    blocks1 = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state1 = HostState(blocks1)
    blocks2 = copy.deepcopy(blocks1)
    host_state2 = HostState(blocks2)
    assert host_state1 == host_state2

# Test inequality of HostState instances due to different blocks
def test_host_state_inequality():
    blocks1 = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state1 = HostState(blocks1)
    blocks2 = [1, 2, 3]
    host_state2 = HostState(blocks2)
    assert not (host_state1 == host_state2)

# Test inequality of HostState instances due to different types
def test_host_state_inequality_type():
    blocks = [
        {'regular': ['task1', 'task2'], 'rescue': [], 'always': []},
        {'regular': ['task3'], 'rescue': ['task4'], 'always': ['task5']}
    ]
    host_state = HostState(blocks)
    assert not (host_state == "not a HostState instance")
