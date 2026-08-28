
import pytest
from ansible.executor.play_iterator import PlayIterator
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def play_iterator():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = {}
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_get_original_task_noop(play_iterator):
    host = 'hostname'
    task = 'task_name'
    result = play_iterator.get_original_task(host, task)
    assert result == (None, None)

@pytest.mark.parametrize("start_at_done", [True, False])
def test_init_with_start_at_task(play_iterator, start_at_done):
    with patch('ansible.executor.play_iterator.HostState') as HostStateMock:
        inventory = MagicMock()
        play_context = MagicMock()
        variable_manager = MagicMock()
        all_vars = {}
        play_iterator = PlayIterator(inventory, MagicMock(), play_context, variable_manager, all_vars, start_at_done)
        
        assert hasattr(play_iterator, '_host_states')
        if start_at_done:
            assert not any(state.did_start_at_task for state in play_iterator._host_states.values())
        else:
            assert all(not state.did_start_at_task for state in play_iterator._host_states.values())

def test_init_without_start_at_task(play_iterator):
    with patch('ansible.executor.play_iterator.HostState') as HostStateMock:
        inventory = MagicMock()
        play_context = MagicMock()
        play_context.start_at_task = None
        variable_manager = MagicMock()
        all_vars = {}
        play_iterator = PlayIterator(inventory, MagicMock(), play_context, variable_manager, all_vars)
        
        assert hasattr(play_iterator, '_host_states')
        assert not any(state.did_start_at_task for state in play_iterator._host_states.values())
