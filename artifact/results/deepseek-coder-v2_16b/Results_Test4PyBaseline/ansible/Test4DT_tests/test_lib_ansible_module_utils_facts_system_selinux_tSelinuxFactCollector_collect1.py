
import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector
from unittest.mock import patch, MagicMock

# Fixture to create an instance of SelinuxFactCollector for testing
@pytest.fixture
def selinux_collector():
    return SelinuxFactCollector()

SELINUX_MODE_DICT = {
    'enforcing': 'enforcing',
    'permissive': 'permissive',
    'disabled': 'disabled'
}

# Test case for collecting SELinux facts with default parameters
def test_collect_default(selinux_collector):
    selinux_facts = selinux_collector.collect()
    assert 'selinux' in selinux_facts
    assert 'status' in selinux_facts['selinux']
    assert isinstance(selinux_facts['selinux']['status'], str)