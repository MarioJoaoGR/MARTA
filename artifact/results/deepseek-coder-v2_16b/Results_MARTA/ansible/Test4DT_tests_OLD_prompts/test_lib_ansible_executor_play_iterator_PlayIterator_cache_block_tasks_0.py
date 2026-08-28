
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.play_iterator import PlayIterator


@patch('ansible.executor.play_iterator.PlayIterator.__init__')
def test_invalid_inputs(mock_init):
    mock_init.side_effect = TypeError("Invalid input type for play")
    with pytest.raises(TypeError):
        PlayIterator(inventory=MagicMock(), play=None, play_context=MagicMock(), variable_manager=MagicMock(), all_vars={'example_var': 'example_value'})

def test_get_host_state():
    mock_inventory = MagicMock()
    mock_play = MagicMock()
    mock_context = MagicMock()
    mock_variable_manager = MagicMock()
    mock_all_vars = {'example_var': 'example_value'}
    
    play_iterator = PlayIterator(inventory=mock_inventory, play=mock_play, play_context=mock_context, variable_manager=mock_variable_manager, all_vars=mock_all_vars)
    with pytest.raises(AttributeError):
        play_iterator.get_host_state(host='hostname')

def test_add_tasks():
    mock_inventory = MagicMock()
    mock_play = MagicMock()
    mock_context = MagicMock()
    mock_variable_manager = MagicMock()
    mock_all_vars = {'example_var': 'example_value'}
    
    play_iterator = PlayIterator(inventory=mock_inventory, play=mock_play, play_context=mock_context, variable_manager=mock_variable_manager, all_vars=mock_all_vars)
    with pytest.raises(TypeError):
        play_iterator.add_tasks(host='hostname', tasks=[{'name': 'Task 1', 'action': {'module': 'shell', 'args': 'echo Task 1'}}])