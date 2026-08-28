
import pytest
from unittest.mock import MagicMock
from ansible.executor.play_iterator import PlayIterator, Block, Task

# Test initialization of PlayIterator without start_at_done
def test_init_without_start_at_done():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = {"key": "value"}
    
    iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    
    assert iterator._play == play
    assert isinstance(iterator._blocks[0], Block)
    assert len(iterator._blocks) > 0
    assert iterator._variable_manager == variable_manager
    assert iterator._host_states == {}

# Test initialization of PlayIterator with start_at_done
def test_init_with_start_at_done():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock(start_at_task="some_task")
    variable_manager = MagicMock()
    all_vars = {"key": "value"}
    
    iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars, start_at_done=True)
    
    assert iterator._play == play
    assert isinstance(iterator._blocks[0], Block)
    assert len(iterator._blocks) > 0
    assert iterator._variable_manager == variable_manager
    assert iterator._host_states == {}

# Test error handling when play is None
def test_error_handling():
    inventory = MagicMock()
    play = None
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = {"key": "value"}
    
    with pytest.raises(AttributeError) as exc_info:
        PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    
    assert str(exc_info.value) == "'NoneType' object has no attribute 'gather_subset'"

# Test edge case when inventory is None
def test_edge_case():
    inventory = None
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = {"key": "value"}
    
    with pytest.raises(AttributeError) as exc_info:
        PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    
    assert str(exc_info.value) == "'NoneType' object has no attribute 'get_hosts'"
