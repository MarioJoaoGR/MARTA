
import pytest
from ansible.executor.play_iterator import HostState, PlayIterator


def test_hoststate_copy():
    blocks = [None]  # Assuming Block is defined elsewhere
    host_state = HostState(blocks)
    copied_host_state = host_state.copy()
    
    assert host_state._blocks == copied_host_state._blocks
    assert host_state.cur_block == copied_host_state.cur_block
    assert host_state.run_state == copied_host_state.run_state
    # Add other assertions for all attributes if necessary

def test_hoststate_equality():
    blocks = [None]  # Assuming Block is defined elsewhere
    host_state1 = HostState(blocks)
    host_state2 = HostState(blocks)
    
    assert host_state1 == host_state2

def test_hoststate_not_equal():
    blocks = [None]  # Assuming Block is defined elsewhere
    host_state1 = HostState(blocks)
    other_object = "not a HostState"
    
    assert not (host_state1 == other_object)