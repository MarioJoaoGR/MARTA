
import pytest
from ansible.executor.play_iterator import HostState, PlayIterator

# Test initialization of HostState
def test_host_state_initialization():
    blocks = []
    host_state = HostState(blocks)
    assert isinstance(host_state, HostState)

# Test getting the current block when no blocks are present
def test_get_current_block_empty():
    host_state = HostState([])
    with pytest.raises(IndexError):
        host_state.get_current_block()

# Test getting the current block when there are blocks available
def test_get_current_block_available():
    blocks = [1, 2, 3]
    host_state = HostState(blocks)
    assert host_state.get_current_block() == 1
