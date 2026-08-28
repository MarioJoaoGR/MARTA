
import pytest
from ansible.executor.play_iterator import PlayIterator

class HostState:
    def __init__(self, blocks):
        self._blocks = blocks[:]
        self.cur_block = 0
        self.cur_regular_task = 0
        self.cur_rescue_task = 0
        self.cur_always_task = 0
        self.run_state = PlayIterator.ITERATING_SETUP
        self.fail_state = PlayIterator.FAILED_NONE
        self.pending_setup = False
        self.tasks_child_state = None
        self.rescue_child_state = None
        self.always_child_state = None
        self.did_rescue = False
        self.did_start_at_task = False

    def copy(self):
        new_host = HostState(self._blocks)
        new_host.cur_block = self.cur_block
        new_host.cur_regular_task = self.cur_regular_task
        new_host.cur_rescue_task = self.cur_rescue_task
        new_host.cur_always_task = self.cur_always_task
        new_host.run_state = self.run_state
        new_host.fail_state = self.fail_state
        new_host.pending_setup = self.pending_setup
        new_host.tasks_child_state = self.tasks_child_state
        new_host.rescue_child_state = self.rescue_child_state
        new_host.always_child_state = self.always_child_state
        new_host.did_rescue = self.did_rescue
        new_host.did_start_at_task = self.did_start_at_task
        return new_host

    def get_current_block(self):
        return self._blocks[self.cur_block]

def test_copy():
    blocks = [1, 2, 3]
    host_state = HostState(blocks)
    new_host = host_state.copy()
    assert new_host._blocks == host_state._blocks
    assert new_host.cur_block == host_state.cur_block
    assert new_host.run_state == host_state.run_state

def test_get_current_block():
    blocks = [1, 2, 3]
    host_state = HostState(blocks)
    current_block = host_state.get_current_block()
    assert current_block == blocks[0]
