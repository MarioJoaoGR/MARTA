# Module: ansible.module_utils.facts.system.selinux
import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

# Fixture to create an instance of SelinuxFactCollector for testing
@pytest.fixture
def selinux_collector():
    return SelinuxFactCollector()

# Test case for collecting SELinux facts with default parameters
def test_collect_default(selinux_collector):
    selinux_facts = selinux_collector.collect()
    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['status'], str)
    assert 'policyvers' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['policyvers'], str)
    assert 'config_mode' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['config_mode'], str)
    assert 'mode' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['mode'], str)
    assert 'type' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['type'], str)
    assert 'selinux_python_present' in selinux_facts
    assert isinstance(selinux_facts['selinux_python_present'], bool)

# Test case for collecting SELinux facts with a custom module and collected facts dictionary
@pytest.mark.parametrize("module, collected_facts", [
    (None, {}),  # Default parameters
    ({}, {})      # Custom module and empty collected facts dictionary
])
def test_collect_custom(selinux_collector, module, collected_facts):
    selinux_facts = selinux_collector.collect(module=module, collected_facts=collected_facts)
    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['status'], str)
    assert 'policyvers' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['policyvers'], str)
    assert 'config_mode' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['config_mode'], str)
    assert 'mode' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['mode'], str)
    assert 'type' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['type'], str)
    assert 'selinux_python_present' in selinux_facts
    assert isinstance(selinux_facts['selinux_python_present'], bool)

# Test case for collecting SELinux facts when the library is missing
def test_collect_missing_library(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', False)
    selinux_collector = SelinuxFactCollector()
    selinux_facts = selinux_collector.collect()
    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert selinux_facts['selinux']['status'] == 'Missing selinux Python library'
    assert 'policyvers' not in selinux_facts['selinux']
    assert 'config_mode' not in selinux_facts['selinux']
    assert 'mode' not in selinux_facts['selinux']
    assert 'type' not in selinux_facts['selinux']
    assert 'selinux_python_present' in selinux_facts
    assert not selinux_facts['selinux_python_present']
