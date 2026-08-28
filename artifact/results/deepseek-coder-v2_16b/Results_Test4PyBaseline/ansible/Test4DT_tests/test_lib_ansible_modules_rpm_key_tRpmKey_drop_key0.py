
# Module: ansible.modules.rpm_key
import pytest
from ansible.module_utils.basic import AnsibleModule
from unittest.mock import patch, MagicMock
import os

# Import the RpmKey class from the specified module
from ansible.modules.rpm_key import RpmKey

@pytest.fixture
def mock_ansible_module():
    # Create a mock AnsibleModule object with necessary parameters
    module = AnsibleModule(argument_spec={
        'state': {'type': 'str', 'default': 'present'},
        'key': {'type': 'str', 'required': True},
        'fingerprint': {'type': 'str'}
    })
    return module

@pytest.fixture
def mock_rpm_path():
    with patch('ansible.modules.rpm_key.RpmKey.get_bin_path') as mock_get_bin_path:
        # Mock the path to the rpm binary
        mock_get_bin_path.return_value = '/usr/bin/rpm'
        yield

@pytest.fixture
def mock_gpg_path():
    with patch('ansible.modules.rpm_key.RpmKey.get_bin_path') as mock_get_bin_path:
        # Mock the path to the gpg binary
        mock_get_bin_path.return_value = '/usr/bin/gpg'
        yield

@pytest.fixture
def rpm_key_instance(mock_ansible_module):
    return RpmKey(mock_ansible_module)

def test_drop_key_present_state(rpm_key_instance, mock_ansible_module):
    # Set up the module parameters for importing a key
    mock_ansible_module.params = {
        'state': 'present',  # The desired state of the key (either 'present' or 'absent')
        'key': 'http://example.com/path/to/keyfile',  # URL to the key file
        'fingerprint': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'  # Fingerprint of the key
    }
    with patch('ansible.modules.rpm_key.RpmKey.fetch_key') as mock_fetch_key, \
         patch('ansible.modules.rpm_key.RpmKey.getkeyid') as mock_getkeyid, \
         patch('ansible.modules.rpm_key.RpmKey.is_keyid') as mock_is_keyid, \
         patch('ansible.modules.rpm_key.RpmKey.normalize_keyid') as mock_normalize_keyid, \
         patch('ansible.modules.rpm_key.RpmKey.import_key') as mock_import_key:
        # Mock the fetch_key method to return a valid key file path
        mock_fetch_key.return_value = '/tmp/keyfile'
        # Mock the getkeyid method to return a valid key ID
        mock_getkeyid.return_value = 'ABCD123456789012'
        # Mock the is_keyid method to return True
        mock_is_keyid.return_value = True
        # Mock the normalize_keyid method to return a normalized key ID
        mock_normalize_keyid.return_value = 'ABCD123456789012'
        
        rpm_key_instance.__init__(mock_ansible_module)
        
        # Assert that the import_key method was called once
        mock_import_key.assert_called_once()

def test_drop_key_absent_state(rpm_key_instance, mock_ansible_module):
    # Set up the module parameters for dropping a key
    mock_ansible_module.params = {
        'state': 'absent',  # The desired state of the key (either 'present' or 'absent')
        'key': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'  # Key ID or fingerprint of the key to be dropped
    }
    
    with patch('ansible.modules.rpm_key.RpmKey.is_key_imported') as mock_is_key_imported, \
         patch('ansible.modules.rpm_key.RpmKey.drop_key') as mock_drop_key:
        # Mock the is_key_imported method to return True
        mock_is_key_imported.return_value = True
        
        rpm_key_instance.__init__(mock_ansible_module)
        
        # Assert that the drop_key method was called once
        mock_drop_key.assert_called_once()

def test_drop_key_not_imported(rpm_key_instance, mock_ansible_module):
    # Set up the module parameters for dropping a key when it is not imported
    mock_ansible_module.params = {
        'state': 'absent',  # The desired state of the key (either 'present' or 'absent')
        'key': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'  # Key ID or fingerprint of the key to be dropped
    }
    
    with patch('ansible.modules.rpm_key.RpmKey.is_key_imported') as mock_is_key_imported, \
         patch('ansible.modules.rpm_key.RpmKey.drop_key'):
        # Mock the is_key_imported method to return False
        mock_is_key_imported.return_value = False
        
        rpm_key_instance.__init__(mock_ansible_module)
        
        # Assert that no key was dropped since it was not imported
        assert not hasattr(rpm_key_instance, 'drop_key')
