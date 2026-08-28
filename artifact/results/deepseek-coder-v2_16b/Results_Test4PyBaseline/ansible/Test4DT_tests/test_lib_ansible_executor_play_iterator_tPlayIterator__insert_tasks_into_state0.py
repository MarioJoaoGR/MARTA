# Module: ansible.executor.play_iterator
import pytest
from ansible.executor.play_iterator import PlayIterator

# Assuming you have initialized inventory, play, play_context, variable_manager, all_vars as sample data
sample_inventory = None  # Replace with actual sample data or initialization
sample_play = None  # Replace with actual sample data or initialization
sample_play_context = None  # Replace with actual sample data or initialization
sample_variable_manager = None  # Replace with actual sample data or initialization
sample_all_vars = {}  # Replace with actual sample data or initialization

@pytest.fixture
def play_iterator():
    return PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars)

def test_get_host_state(play_iterator):
    host_state = play_iterator.get_host_state('host1')
    assert isinstance(host_state, HostState), "Expected HostState object"

def test_get_next_task_for_host(play_iterator):
    task, _ = play_iterator.get_next_task_for_host('host1', peek=True)
    assert task is not None, "Expected a task to be returned"

def test_mark_host_failed(play_iterator):
    initial_state = play_iterator._host_states['host1'].run_state
    play_iterator.mark_host_failed('host1')
    assert play_iterator._host_states['host1'].run_state != initial_state, "Expected run state to change upon marking host as failed"

def test_insert_tasks_into_state(play_iterator):
    task_list = [Task(block=Block(play=sample_play))]  # Replace with actual sample data or initialization
    state = HostState(blocks=[Block(play=sample_play)])  # Replace with actual sample data or initialization
    new_state = play_iterator._insert_tasks_into_state(state, task_list)
    assert len(new_state.tasks) == len(task_list), "Expected tasks to be inserted into the state"
