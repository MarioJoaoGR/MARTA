# Module: ansible.module_utils.facts.system.service_mgr
import pytest
from your_module import ServiceMgrFactCollector

# Fixture for creating an instance of ServiceMgrFactCollector
@pytest.fixture
def collector():
    return ServiceMgrFactCollector()

# Test case 1: Default Usage
def test_default_usage(collector):
    result = collector.collect()
    assert isinstance(result, dict), "Expected a dictionary as the result"
    assert 'service_mgr' in result, "Expected 'service_mgr' key in the result dictionary"
    assert result['service_mgr'] == 'service', "Expected default value 'service' for service_mgr"

# Test case 2: With Mock Module for Testing
@pytest.fixture
def mock_module():
    class MockModule:
        def run_command(self, command, use_unsafe_shell=False):
            return (0, "systemd", "")  # Simulate a successful command execution returning 'systemd'
    return MockModule()

def test_with_mock_module(collector, mock_module):
    result = collector.collect(module=mock_module)
    assert isinstance(result, dict), "Expected a dictionary as the result"
    assert 'service_mgr' in result, "Expected 'service_mgr' key in the result dictionary"
    assert result['service_mgr'] == 'systemd', "Expected 'systemd' for service_mgr when using mock module"

# Test case 3: With Collected Facts
@pytest.fixture
def collected_facts():
    return {
        'ansible_distribution': 'Ubuntu',
        'ansible_system': 'Linux'
    }

def test_with_collected_facts(collector, mock_module, collected_facts):
    result = collector.collect(module=mock_module, collected_facts=collected_facts)
    assert isinstance(result, dict), "Expected a dictionary as the result"
    assert 'service_mgr' in result, "Expected 'service_mgr' key in the result dictionary"
    assert result['service_mgr'] == 'systemd', "Expected 'systemd' for service_mgr when using mock module and collected facts"

# Test case 4: With No Module Provided
def test_no_module_provided(collector):
    result = collector.collect()
    assert isinstance(result, dict), "Expected a dictionary as the result"
    assert 'service_mgr' in result, "Expected 'service_mgr' key in the result dictionary"
    assert result['service_mgr'] == 'service', "Expected default value 'service' for service_mgr when no module is provided"
