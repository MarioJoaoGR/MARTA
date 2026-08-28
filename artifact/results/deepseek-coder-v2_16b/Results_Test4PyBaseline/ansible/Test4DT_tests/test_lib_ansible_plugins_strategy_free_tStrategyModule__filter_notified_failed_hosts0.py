# Module: ansible.plugins.strategy.free
import pytest
from your_module import TaskQueueManager, StrategyModule

# Assuming TaskQueueManager and StrategyModule are defined elsewhere in your module or imported

def test_strategy_module_initialization():
    tqm = TaskQueueManager()  # Initialize the task queue manager
    strategy_module = StrategyModule(tqm)  # Pass tqm to initialize StrategyModule
    
    assert hasattr(strategy_module, '_host_pinned'), "StrategyModule instance should have _host_pinned attribute"
    assert not strategy_module._host_pinned, "_host_pinned should be False initially"

def test_filter_notified_failed_hosts():
    tqm = TaskQueueManager()  # Initialize the task queue manager
    strategy_module = StrategyModule(tqm)  # Pass tqm to initialize StrategyModule
    
    class MockIterator:
        def is_failed(self, host):
            return host == 'host1'
    
    notified_hosts = ['host1', 'host2', 'host3']
    failed_hosts = strategy_module._filter_notified_failed_hosts(MockIterator(), notified_hosts)
    
    assert len(failed_hosts) == 1, "Expected one host to be marked as failed"
    assert 'host1' in failed_hosts, "Expected 'host1' to be in the list of failed hosts"

def test_filter_notified_failed_hosts_no_failure():
    tqm = TaskQueueManager()  # Initialize the task queue manager
    strategy_module = StrategyModule(tqm)  # Pass tqm to initialize StrategyModule
    
    class MockIterator:
        def is_failed(self, host):
            return False
    
    notified_hosts = ['host1', 'host2', 'host3']
    failed_hosts = strategy_module._filter_notified_failed_hosts(MockIterator(), notified_hosts)
    
    assert len(failed_hosts) == 0, "Expected no hosts to be marked as failed"

def test_filter_notified_failed_hosts_all_failure():
    tqm = TaskQueueManager()  # Initialize the task queue manager
    strategy_module = StrategyModule(tqm)  # Pass tqm to initialize StrategyModule
    
    class MockIterator:
        def is_failed(self, host):
            return True
    
    notified_hosts = ['host1', 'host2', 'host3']
    failed_hosts = strategy_module._filter_notified_failed_hosts(MockIterator(), notified_hosts)
    
    assert len(failed_hosts) == 3, "Expected all hosts to be marked as failed"

def test_filter_notified_failed_hosts_mixed():
    tqm = TaskQueueManager()  # Initialize the task queue manager
    strategy_module = StrategyModule(tqm)  # Pass tqm to initialize StrategyModule
    
    class MockIterator:
        def is_failed(self, host):
            return host == 'host2'
    
    notified_hosts = ['host1', 'host2', 'host3']
    failed_hosts = strategy_module._filter_notified_failed_hosts(MockIterator(), notified_hosts)
    
    assert len(failed_hosts) == 1, "Expected one host to be marked as failed"
    assert 'host2' in failed_hosts, "Expected 'host2' to be in the list of failed hosts"
