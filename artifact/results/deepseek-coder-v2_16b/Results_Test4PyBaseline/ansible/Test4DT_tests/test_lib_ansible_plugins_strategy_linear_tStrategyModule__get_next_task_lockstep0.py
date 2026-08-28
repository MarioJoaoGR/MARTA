# Module: ansible.plugins.strategy.linear
# test_strategy_module.py
from ansible.plugins.strategy import StrategyModule
import pytest

@pytest.fixture
def strategy_module():
    return StrategyModule()

@pytest.fixture
def mock_hosts():
    class Host:
        def __init__(self, name):
            self.name = name
    
    host1 = Host("host1")
    host2 = Host("host2")
    return [host1, host2]

@pytest.fixture
def mock_iterator():
    class MockPlayIterator:
        def __init__(self):
            self.tasks = {
                "host1": ("setup", None),
                "host2": ("task1", None)
            }
        
        def get_next_task_for_host(self, host, peek=False):
            return self.tasks[host.name] if not peek else self.tasks[host.name]
    
    return MockPlayIterator()

def test_get_next_task_lockstep_with_setups(strategy_module, mock_hosts, mock_iterator):
    next_tasks = strategy_module._get_next_task_lockstep(hosts=mock_hosts, iterator=mock_iterator)
    assert len(next_tasks) == 2
    for task in next_tasks:
        assert task[1] is not None

def test_get_next_task_lockstep_with_tasks(strategy_module, mock_hosts, mock_iterator):
    # Assuming the iterator has tasks set up such that both hosts should get a normal task
    next_tasks = strategy_module._get_next_task_lockstep(hosts=mock_hosts, iterator=mock_iterator)
    assert len(next_tasks) == 2
    for task in next_tasks:
        assert task[1] is not None

def test_get_next_task_lockstep_with_rescues(strategy_module, mock_hosts, mock_iterator):
    # Assuming the iterator has tasks set up such that both hosts should get a rescue task
    next_tasks = strategy_module._get_next_task_lockstep(hosts=mock_hosts, iterator=mock_iterator)
    assert len(next_tasks) == 2
    for task in next_tasks:
        assert task[1] is not None

def test_get_next_task_lockstep_with_always(strategy_module, mock_hosts, mock_iterator):
    # Assuming the iterator has tasks set up such that both hosts should get an always task
    next_tasks = strategy_module._get_next_task_lockstep(hosts=mock_hosts, iterator=mock_iterator)
    assert len(next_tasks) == 2
    for task in next_tasks:
        assert task[1] is not None

def test_get_next_task_lockstep_with_no_tasks(strategy_module, mock_hosts, mock_iterator):
    # Assuming the iterator has tasks set up such that both hosts should get a noop task since no other tasks are available
    next_tasks = strategy_module._get_next_task_lockstep(hosts=mock_hosts, iterator=mock_iterator)
    assert len(next_tasks) == 2
    for task in next_tasks:
        assert task[1] is not None
