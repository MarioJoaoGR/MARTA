# Module: ansible.executor.play_iterator
# test_play_iterator.py
from ansible.executor.play_iterator import PlayIterator
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.playbook.play_context import PlayContext
import pytest

@pytest.fixture
def setup():
    # Initialize inventory, loader, variable manager, and passwords
    inventory = InventoryManager(host_list='hosts')
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    passwords = {}

    # Define play configuration
    play = Play.from_dict({
        'name': 'Example Play',
        'hosts': 'all',
        'gather_facts': 'no'
    })

    # Define play context
    play_context = PlayContext(loader=loader, inventory=inventory)

    return {
        'inventory': inventory,
        'loader': loader,
        'variable_manager': variable_manager,
        'passwords': passwords,
        'play': play,
        'play_context': play_context
    }

def test_init(setup):
    # Initialize PlayIterator with the necessary parameters
    iterator = PlayIterator(
        inventory=setup['inventory'],
        play=setup['play'],
        play_context=setup['play_context'],
        variable_manager=setup['variable_manager'],
        all_vars={},
        start_at_done=False
    )
    
    assert iterator._play == setup['play']
    assert isinstance(iterator._blocks, list)
    assert isinstance(iterator._host_states, dict)
    assert iterator.batch_size > 0
    assert not iterator.end_play

def test_get_host_state(setup):
    # Initialize PlayIterator with the necessary parameters
    iterator = PlayIterator(
        inventory=setup['inventory'],
        play=setup['play'],
        play_context=setup['play_context'],
        variable_manager=setup['variable_manager'],
        all_vars={},
        start_at_done=False
    )
    
    # Get host state for a known host
    host = setup['inventory'].get_hosts('host1')[0]
    host_state = iterator.get_host_state(host)
    assert isinstance(host_state, HostState)
    
    # Get host state for an unknown host (should create a stub state)
    unknown_host = setup['inventory'].get_hosts('unknown')[0]
    unknown_host_state = iterator.get_host_state(unknown_host)
    assert isinstance(unknown_host_state, HostState)
    assert not unknown_host_state._tasks

def test_get_next_task_for_host(setup):
    # Initialize PlayIterator with the necessary parameters
    iterator = PlayIterator(
        inventory=setup['inventory'],
        play=setup['play'],
        play_context=setup['play_context'],
        variable_manager=setup['variable_manager'],
        all_vars={},
        start_at_done=False
    )
    
    # Get next task for a known host (should return the first task)
    host = setup['inventory'].get_hosts('host1')[0]
    (s, task) = iterator.get_next_task_for_host(host)
    assert s.run_state == PlayIterator.ITERATING_SETUP
    assert isinstance(task, Task)
    
    # Get next task for a known host with peek=True (should not advance the state)
    (s, task) = iterator.get_next_task_for_host(host, peek=True)
    assert s.run_state == PlayIterator.ITERATING_SETUP
    assert isinstance(task, Task)
    
    # Get next task for a known host with no tasks (should return complete state)
    iterator._blocks = []  # Remove all tasks to simulate empty play
    (s, task) = iterator.get_next_task_for_host(host)
    assert s.run_state == PlayIterator.ITERATING_COMPLETE
    assert not task
