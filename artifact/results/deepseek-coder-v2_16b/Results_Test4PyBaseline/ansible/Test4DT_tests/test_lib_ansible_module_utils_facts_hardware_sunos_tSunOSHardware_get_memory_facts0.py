
# Module: ansible.module_utils.facts.hardware.sunos
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.basic import AnsibleModule
try:
    from lib.ansible.module_utils.facts.hardware.base import SunOSHardware
except ImportError:
    # If the import fails, skip this test or handle it appropriately
    pytestmark = pytest.mark.skip(reason="Unable to import 'lib.ansible.module_utils.facts.hardware.base'")

# Mock the module and its run_command method
class MockModule(AnsibleModule):
    def __init__(self):
        super().__init__(argument_spec={})
    
    def run_command(self, command):
        if command[0] == "/usr/sbin/prtconf":
            return (0, "Memory size 16384 MB\n", "")
        elif command[0] == "/usr/sbin/swap -s":
            return (0, "Total: 256MB allocated, 128MB reserved, 128MB used, 0MB free\n", "")

# Test the SunOSHardware class and its get_memory_facts method
def test_get_memory_facts():
    # Create a mock module instance
    mock_module = MockModule()
    
    # Instantiate the SunOSHardware class with the mock module
    hardware = SunOSHardware(module=mock_module)
    
    # Call the get_memory_facts method to retrieve memory facts
    memory_facts = hardware.get_memory_facts()
    
    # Assert that the output matches the expected result
    assert memory_facts == {
        'memtotal_mb': 16384,
        'swapfree_mb': 0,
        'swaptotal_mb': 256,
        'swap_allocated_mb': 128,
        'swap_reserved_mb': 128
    }
