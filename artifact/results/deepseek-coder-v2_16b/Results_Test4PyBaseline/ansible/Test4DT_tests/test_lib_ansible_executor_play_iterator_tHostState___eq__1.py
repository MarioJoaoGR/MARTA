
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