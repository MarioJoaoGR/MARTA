
import pytest
from ansible.executor.play_iterator import PlayIterator
from unittest.mock import MagicMock

@pytest.fixture(scope="module")
def play_iterator():
    inventory = MagicMock()
    play = MagicMock()
    play_context = {'start_at_task': None}
    variable_manager = MagicMock()
    all_vars = {}
    return PlayIterator(inventory=inventory, play=play, play_context=play_context, variable_manager=variable_manager, all_vars=all_vars)

def test_initialize_without_start_at_task(play_iterator):
    assert play_iterator.batch_size == len(play_iterator._host_states)
    assert not any(state.did_start_at_task for state in play_iterator._host_states.values())

def test_initialize_with_start_at_task(play_iterator):
    inventory = MagicMock()
    play = MagicMock()
    play_context = {'start_at_task': 'specific_task'}
    variable_manager = MagicMock()
    all_vars = {}

    iterator = PlayIterator(inventory=inventory, play=play, play_context=play_context, variable_manager=variable_manager, all_vars=all_vars)

    assert iterator.batch_size == len(inventory.get_hosts.return_value)
    assert not any(state.did_start_at_task for state in iterator._host_states.values())

def test_initialize_with_start_at_done(play_iterator):
    inventory = MagicMock()
    play = MagicMock()
    play_context = {'start_at_task': None}
    variable_manager = MagicMock()
    all_vars = {}

    iterator = PlayIterator(inventory=inventory, play=play, play_context=play_context, variable_manager=variable_manager, all_vars=all_vars, start_at_done=True)

    assert iterator.batch_size == len(inventory.get_hosts.return_value)
    assert not any(state.did_start_at_task for state in iterator._host_states.values())
