# Module: ansible.module_utils.facts.system.caps
import pytest
from ansible.module_utils import basic

# Mock the SystemCapabilitiesFactCollector class and its collect method for testing
class MockModule:
    def get_bin_path(self, binary_name):
        if binary_name == 'capsh':
            return '/usr/local/bin/capsh'  # Assuming the capsh binary exists at this path
    
    def run_command(self, command, errors='surrogate_then_replace'):
        if command[0] == '/usr/local/bin/capsh' and command[1] == '--print':
            return (0, "Current: =ep\nCapabilities: cap_chown,cap_dac_override", "")  # Mock output for the capsh command

class MockModuleNoCapsh:
    def get_bin_path(self, binary_name):
        if binary_name == 'capsh':
            return None  # Assuming the capsh binary does not exist
    
    def run_command(self, command, errors='surrogate_then_replace'):
        pass

# Test cases for SystemCapabilitiesFactCollector's collect method
def test_collect_with_module():
    module = MockModule()
    fact_collector = SystemCapabilitiesFactCollector()
    facts = fact_collector.collect(module=module)
    assert 'system_capabilities_enforced' in facts
    assert 'system_capabilities' in facts
    assert facts['system_capabilities'] == ['cap_chown', 'cap_dac_override']
    assert facts['system_capabilities_enforced'] == 'False'

def test_collect_without_module():
    fact_collector = SystemCapabilitiesFactCollector()
    facts = fact_collector.collect(module=None)
    assert not facts  # Should return an empty dictionary if no module is provided

def test_collect_no_capsh():
    module = MockModuleNoCapsh()
    fact_collector = SystemCapabilitiesFactCollector()
    facts = fact_collector.collect(module=module)
    assert not facts  # Should return an empty dictionary if capsh does not exist
