
import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play():
    # Create an instance of the Play class for testing
    return Play()

# Test case to check if hosts are correctly set
def test_set_hosts(play):
    play._hosts = ['host1', 'host2']
    assert play._hosts == ['host1', 'host2'], "Hosts should be correctly set"

# Test case to check if gather facts is correctly set
def test_set_gather_facts(play):
    play._gather_facts = True
    assert play._gather_facts is True, "Gather facts should be correctly set"

# Test case to check if roles are correctly added (should raise AttributeError)
def test_add_roles(play):
    with pytest.raises(AttributeError):
        play._roles.append('role1')

# Test case to check if tasks are correctly added (should raise AttributeError)
def test_add_tasks(play):
    with pytest.raises(AttributeError):
        play._tasks.append({'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}})

# Test case to check if getting variables returns a copy
def test_get_vars(play):
    play.vars = {'var1': 'value1', 'var2': 'value2'}
    vars_copy = play.get_vars()
    assert play.vars == vars_copy, "Getting variables should return a copy"
    assert play.vars is not vars_copy, "The original and the copied variables should be different objects"

# Test case to check if gather subset is correctly set
def test_set_gather_subset(play):
    play._gather_subset = ['network']
    assert play._gather_subset == ['network'], "Gather subset should be correctly set"

# Test case to check if gather timeout is correctly set
def test_set_gather_timeout(play):
    play._gather_timeout = 30
    assert play._gather_timeout == 30, "Gather timeout should be correctly set"

# Test case to check if fact path is correctly set
def test_set_fact_path(play):
    play._fact_path = '/path/to/facts'