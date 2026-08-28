
import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

# Fixture to create an instance of SelinuxFactCollector for testing
@pytest.fixture
def selinux_collector():
    return SelinuxFactCollector()

# Test case for initializing the facts dictionary and selinux_facts
def test_collect_initialization(selinux_collector):
    selinux_facts = selinux_collector.collect()
    assert 'selinux' in selinux_facts
    assert isinstance(selinux_facts['selinux'], dict)