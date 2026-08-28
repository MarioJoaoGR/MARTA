
import pytest
from ansible.cli.adhoc import AdHocCLI

@pytest.fixture
def valid_instance():
    return AdHocCLI()

# Test Scenario 1: Valid inputs - happy path
def test_valid_inputs_happy_path(valid_instance):
    pattern = ['host1', 'host2']
    async_val = 60
    poll = 30
    playbook = valid_instance._play_ds(pattern, async_val, poll)
    
    assert playbook['name'] == "Ansible Ad-Hoc"
    assert playbook['hosts'] == pattern
    assert playbook['gather_facts'] == 'no'
    assert len(playbook['tasks']) == 1
    task = playbook['tasks'][0]
    assert task['action']['module'] == context.CLIARGS['module_name']
    assert task['timeout'] == context.CLIARGS['task_timeout']
    assert 'async_val' in task
    assert task['async_val'] == async_val
    assert 'poll' in task
    assert task['poll'] == poll

# Test Scenario 2: Edge cases - None for pattern, empty list for pattern, invalid async_val or poll values
@pytest.mark.parametrize("pattern, async_val, poll", [
    (None, 60, 30),  # None for pattern
    ([], 60, 30),   # Empty list for pattern
    ('host1', None, 30),  # Invalid async_val
    ('host1', 60, None)   # Invalid poll
])
def test_edge_cases(valid_instance, pattern, async_val, poll):
    with pytest.raises(TypeError):  # Since the method expects specific types for parameters
        valid_instance._play_ds(pattern, async_val, poll)

# Test Scenario 3: Invalid inputs - raising ValueError with invalid inputs like non-integer async_val or poll
def test_invalid_inputs_error_handling(valid_instance):
    pattern = ['host1']
    async_val = 'not_an_int'
    poll = 'also_not_an_int'
    
    with pytest.raises(ValueError):  # Expecting ValueError due to invalid types for async_val and poll
        valid_instance._play_ds(pattern, async_val, poll)
