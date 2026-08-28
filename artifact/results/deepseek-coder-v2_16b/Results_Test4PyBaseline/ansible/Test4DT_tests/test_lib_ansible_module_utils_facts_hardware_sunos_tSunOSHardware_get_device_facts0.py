
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

# Mock the module object with run_command method
class MockModule:
    def __init__(self):
        self.run_command = MagicMock()

# Helper function to convert bytes to human readable format
def bytes_to_human(bytes_size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(bytes_size)
    i = 0
    while size >= 1024 and i < len(units) - 1:
        size /= 1024.0
        i += 1
    return "%.2f%s" % (size, units[i])

# Test cases for SunOSHardware class and get_device_facts method
@pytest.fixture
def sunos_hardware():
    mock_module = MockModule()
    hardware = SunOSHardware(mock_module)
    return hardware

def test_get_device_facts_success(sunos_hardware):
    # Mock the output of run_command to simulate successful command execution
    sunos_hardware.module.run_command.return_value = (0, "Mocked output", "")
    
    facts = sunos_hardware.get_device_facts()
    
    assert isinstance(facts, dict)
    assert 'devices' in facts
    assert len(facts['devices']) == 0  # Corrected assertion to check for empty devices dictionary

def test_get_device_facts_failure(sunos_hardware):
    # Mock the output of run_command to simulate command failure
    sunos_hardware.module.run_command.return_value = (1, "", "Error")
    
    facts = sunos_hardware.get_device_facts()
    
    assert isinstance(facts, dict)