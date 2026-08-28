# Module: ansible.executor.play_iterator
# test_play_iterator.py
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.play_iterator import PlayIterator
from ansible.vars.manager import VariableManager
import pytest

# Assuming you have initialized the necessary objects like inventory, play, etc.
@pytest.fixture(scope="module")
def setup_play_iterator():
    inventory = Inventory(host_list=['localhost'])
    play = Play()  # You need to set up your play object with appropriate tasks and blocks
    play_context = {}  # Set up your play context as needed
    variable_manager = VariableManager()
    all_vars = {}  # Initialize all variables dictionary if needed

    # Example call to initialize a PlayIterator object
    return PlayIterator(inventory=inventory, play=play, play_context=play_context, variable_manager=variable_manager, all_vars=all_vars)

def test_get_next_task_from_state_setup(setup_play_iterator):
    play_iterator = setup_play_iterator
    host = Host(name='localhost')  # Assuming you have a Host class and can create a host object
    state = HostState()
    
    # Test the initial run_state is ITERATING_SETUP
    (s, task) = play_iterator._get_next_task_from_state(state, host)
    assert s.run_state == PlayIterator.ITERATING_SETUP
    assert s.pending_setup is True
    
    # Test gathering facts when run_state is ITERATING_SETUP
    (s, task) = play_iterator._get_next_task_from_state(s, host)
    assert s.run_state == PlayIterator.ITERATING_TASKS
    assert s.pending_setup is False
    
def test_get_next_task_from_state_tasks(setup_play_iterator):
    play_iterator = setup_play_iterator
    host = Host(name='localhost')  # Assuming you have a Host class and can create a host object
    state = HostState()
    
    # Test the initial run_state is ITERATING_SETUP
    (s, task) = play_iterator._get_next_task_from_state(state, host)
    assert s.run_state == PlayIterator.ITERATING_TASKS
    
    # Add a task to the setup block for testing
    setup_block = Block(play=play_iterator._play)
    setup_block.run_once = False
    gather_facts_task = Task(block=setup_block)
    gather_facts_task.action = 'gather_facts'
    gather_facts_task.name = 'Gathering Facts'
    gather_facts_task.args = {'gather_subset': ['all']}
    setup_block.block = [gather_facts_task]
    
    # Test getting the next task when run_state is ITERATING_TASKS
    (s, task) = play_iterator._get_next_task_from_state(s, host)
    assert s.run_state == PlayIterator.ITERATING_TASKS
    assert isinstance(task, Task)
    
def test_get_next_task_from_state_rescue(setup_play_iterator):
    play_iterator = setup_play_iterator
    host = Host(name='localhost')  # Assuming you have a Host class and can create a host object
    state = HostState()
    
    # Test the initial run_state is ITERATING_SETUP
    (s, task) = play_iterator._get_next_task_from_state(state, host)
    assert s.run_state == PlayIterator.ITERATING_TASKS
    
    # Add a rescue block for testing
    setup_block = Block(play=play_iterator._play)
    setup_block.run_once = False
    gather_facts_task = Task(block=setup_block)
    gather_facts_task.action = 'gather_facts'
    gather_facts_task.name = 'Gathering Facts'
    gather_facts_task.args = {'gather_subset': ['all']}
    setup_block.rescue = [gather_facts_task]
    
    # Test getting the next task when run_state is ITERATING_RESCUE
    (s, task) = play_iterator._get_next_task_from_state(s, host)
    assert s.run_state == PlayIterator.ITERATING_RESCUE
    assert isinstance(task, Task)
    
def test_get_next_task_from_state_always(setup_play_iterator):
    play_iterator = setup_play_iterator
    host = Host(name='localhost')  # Assuming you have a Host class and can create a host object
    state = HostState()
    
    # Test the initial run_state is ITERATING_SETUP
    (s, task) = play_iterator._get_next_task_from_state(state, host)
    assert s.run_state == PlayIterator.ITERATING_TASKS
    
    # Add an always block for testing
    setup_block = Block(play=play_iterator._play)
    setup_block.run_once = False
    gather_facts_task = Task(block=setup_block)
    gather_facts_task.action = 'gather_facts'
    gather_facts_task.name = 'Gathering Facts'
    gather_facts_task.args = {'gather_subset': ['all']}
    setup_block.always = [gather_facts_task]
    
    # Test getting the next task when run_state is ITERATING_ALWAYS
    (s, task) = play_iterator._get_next_task_from_state(s, host)
    assert s.run_state == PlayIterator.ITERATING_ALWAYS
    assert isinstance(task, Task)
    
def test_get_next_task_from_state_complete(setup_play_iterator):
    play_iterator = setup_play_iterator
    host = Host(name='localhost')  # Assuming you have a Host class and can create a host object
    state = HostState()
    
    # Test the initial run_state is ITERATING_SETUP
    (s, task) = play_iterator._get_next_task_from_state(state, host)
    assert s.run_state == PlayIterator.ITERATING_TASKS
    
    # Add a task that will cause the state to complete
    setup_block = Block(play=play_iterator._play)
    setup_block.run_once = False
    gather_facts_task = Task(block=setup_block)
    gather_facts_task.action = 'gather_facts'
    gather_facts_task.name = 'Gathering Facts'
    gather_facts_task.args = {'gather_subset': ['all']}
    setup_block.block = [gather_facts_task]
    
    # Test getting the next task when run_state is ITERATING_COMPLETE
    (s, task) = play_iterator._get_next_task_from_state(s, host)
    assert s.run_state == PlayIterator.ITERATING_COMPLETE
    assert task is None
