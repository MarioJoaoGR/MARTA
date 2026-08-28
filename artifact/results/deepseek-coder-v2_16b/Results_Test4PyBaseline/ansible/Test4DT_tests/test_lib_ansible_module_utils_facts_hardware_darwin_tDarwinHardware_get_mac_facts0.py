
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.basic import AnsibleModule
try:
    from darwinhardware import DarwinHardware
except ImportError:
    pytest.skip("Darwin hardware module not available", allow_module_level=True)

# Test case for retrieving macOS hardware facts with specific sysctl data
def test_get_mac_facts_with_specific_sysctl():
    module = AnsibleModule(argument_spec={})
    darwin_hardware = DarwinHardware(module=module, sysctl={'kern.osversion': '10.15.7', 'kern.osrevision': '19H2'})
    
    with patch('darwinhardware.DarwinHardware.get_mac_facts') as mock_get_mac_facts:
        darwin_hardware.get_mac_facts()
        mock_get_mac_facts.assert_called_once()
        assert darwin_hardware.sysctl['kern.osversion'] == '10.15.7'
        assert darwin_hardware.sysctl['kern.osrevision'] == '19H2'

# Test case for retrieving macOS hardware facts with different sysctl data
def test_get_mac_facts_with_different_sysctl():
    module = AnsibleModule(argument_spec={})
    darwin_hardware = DarwinHardware(module=module, sysctl={'kern.osversion': '11.0', 'kern.osrevision': '20A388'})
    
    with patch('darwinhardware.DarwinHardware.get_mac_facts') as mock_get_mac_facts:
        darwin_hardware.get_mac_facts()
        mock_get_mac_facts.assert_called_once()
        assert darwin_hardware.sysctl['kern.osversion'] == '11.0'
        assert darwin_hardware.sysctl['kern.osrevision'] == '20A388'

# Test case for retrieving macOS hardware facts without sysctl data
def test_get_mac_facts_without_sysctl():
    module = AnsibleModule(argument_spec={})
    darwin_hardware = DarwinHardware(module=module)
    
    with patch('darwinhardware.DarwinHardware.get_mac_facts') as mock_get_mac_facts:
        darwin_hardware.get_mac_facts()
        mock_get_mac_facts.assert_called_once()
        assert 'osversion' not in darwin_hardware.sysctl
        assert 'osrevision' not in darwin_hardware.sysctl

# Test case for retrieving macOS hardware facts with run_command returning an error
def test_get_mac_facts_with_run_command_error():
    module = AnsibleModule(argument_spec={})
    darwin_hardware = DarwinHardware(module=module, sysctl={'kern.osversion': '10.15.7', 'kern.osrevision': '19H2'})
    
    with patch('darwinhardware.DarwinHardware.module.run_command', return_value=(1, '', '')):
        with pytest.raises(Exception):
            darwin_hardware.get_mac_facts()
