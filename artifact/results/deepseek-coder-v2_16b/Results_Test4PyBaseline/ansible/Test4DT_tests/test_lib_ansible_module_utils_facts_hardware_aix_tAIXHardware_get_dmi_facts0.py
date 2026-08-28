
# Module: ansible.module_utils.facts.hardware.aix
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

# Fixture to create a mock instance of AIXHardware with AnsibleModule
@pytest.fixture
def aix_hardware():
    aix_hardware = AIXHardware(module=MagicMock())
    return aix_hardware

# Test case for get_dmi_facts method when lsconf is not available
def test_get_dmi_facts_no_lsconf(aix_hardware):
    # Mock the run_command to simulate a successful command execution with output
    aix_hardware.module.run_command.return_value = (0, "IBM, 7.1", "")
    aix_hardware.module.get_bin_path.return_value = None
    
    # Call the method under test
    dmi_facts = aix_hardware.get_dmi_facts()
    
    # Assertions to validate the output and behavior of the method
    assert 'firmware_version' in dmi_facts
    assert dmi_facts['firmware_version'] == "7.1"
    assert 'product_serial' not in dmi_facts
    assert 'lpar_info' not in dmi_facts
    assert 'product_name' not in dmi_facts

# Test case for get_dmi_facts method when lsconf is available and provides relevant information
def test_get_dmi_facts_with_lsconf(aix_hardware):
    # Mock the run_command to simulate a successful command execution with output
    aix_hardware.module.run_command.side_effect = [
        (0, "IBM, 7.1", ""),  # for lsattr command
        (0, "Machine Serial Number: ABC123\nLPAR Info: DEF456\nSystem Model: AIX Server", "")  # for lsconf command
    ]
    aix_hardware.module.get_bin_path.return_value = "lsconf"
    
    # Call the method under test
    dmi_facts = aix_hardware.get_dmi_facts()
    
    # Assertions to validate the output and behavior of the method
    assert 'firmware_version' in dmi_facts
    assert dmi_facts['firmware_version'] == "7.1"
    assert 'product_serial' in dmi_facts
    assert dmi_facts['product_serial'] == "ABC123"
    assert 'lpar_info' in dmi_facts
    assert dmi_facts['lpar_info'] == "DEF456"
    assert 'product_name' in dmi_facts
    assert dmi_facts['product_name'] == "AIX Server"
