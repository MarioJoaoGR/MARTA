# Module: ansible.executor.play_iterator
# test_play_iterator.py
from your_module import PlayIterator

def test_basic_initialization():
    iterator = PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars)
    assert isinstance(iterator, PlayIterator), "Initialization should create a PlayIterator instance"

def test_initialization_with_start_at_done():
    iterator = PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars, start_at_done=True)
    assert isinstance(iterator, PlayIterator), "Initialization with start_at_done should create a PlayIterator instance"

def test_iterating_over_tasks_for_specific_host():
    iterator = PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars)
    host = "specific_host"
    task_list = []
    while True:
        (s, task) = iterator.get_next_task_for_host(host, peek=False)
        if s == PlayIterator.ITERATING_COMPLETE:
            break
        task_list.append(task)
    assert len(task_list) > 0, "Tasks should be iterated over for the specific host"

def test_marking_host_as_failed():
    iterator = PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars)
    host = "specific_host"
    iterator.mark_host_failed(host)
    assert iterator._host_states[host].run_state == PlayIterator.FAILED_TASKS, "Host should be marked as failed"

def test_getting_the_state_of_a_specific_host():
    iterator = PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars)
    host = "specific_host"
    host_state = iterator.get_host_state(host)
    assert isinstance(host_state, HostState), "The state of the specific host should be a HostState instance"

def test_checking_if_iteration_is_complete():
    iterator = PlayIterator(inventory=sample_inventory, play=sample_play, play_context=sample_play_context, variable_manager=sample_variable_manager, all_vars=sample_all_vars)
    assert not iterator.end_play, "Iteration should not be complete initially"
