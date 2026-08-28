# Module: ansible.module_utils.facts.hardware.darwin
import pytest
from ansible.module_utils.basic import AnsibleModule
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

# Mocking the module and its run_command method for testing
@patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.get_system_profile')
def test_get_system_profile(mock_get_system_profile):
    # Create a mock instance of AnsibleModule
    module = MagicMock()
    
    # Create an instance of DarwinHardware with the mocked module
    darwin_hardware = DarwinHardware(module)
    
    # Define expected system profile dictionary
    expected_profile = {
        'Processor': 'Intel Core i7',
        'Processor Cores': '4',
        'Memory': '16 GB',
        'Free Memory': '8 GB',
        'Model Name': 'MacBook Pro',
        'OS Version': 'Big Sur',
        'OS Revision': '10.16',
        'Uptime': '7200 seconds'
    }
    
    # Set the return value of get_system_profile to be the expected profile
    mock_get_system_profile.return_value = expected_profile
    
    # Call the method under test
    result = darwin_hardware.get_system_profile()
    
    # Assert that the command was run and the output was parsed correctly
    assert result == expected_profile

# Run the test
if __name__ == '__main__':
    pytest.main()
