
# Module: ansible.modules.rpm_key
# test_rpm_key.py
from ansible.module_utils.basic import AnsibleModule
import pytest
import subprocess
import os

class RpmKey:
    def __init__(self, module):
        self.module = module
    
    @staticmethod
    def fetch_key(url_or_path):
        # Implement the logic to fetch or read a key from a given URL or local path
        pass
    
    @staticmethod
    def is_key_imported(fingerprint):
        # Implement the logic to check if a key with the given fingerprint is imported
        pass

@pytest.fixture
def module():
    return AnsibleModule(argument_spec={
        'state': {'type': 'str', 'default': 'present'},
        'key': {'type': 'str', 'required': True},
        'fingerprint': {'type': 'str'}
    })

@pytest.fixture
def rpm_key(module):
    return RpmKey(module)

def test_import_key_from_url(mocker, module):
    # Mock the fetch_key method to return a temporary file path
    mocker.patch('ansible.modules.rpm_key.RpmKey.fetch_key', return_value='/tmp/keyfile')
    # Initialize RpmKey with module parameters for importing a key from a URL
    module.params = {
        'state': 'present',
        'key': 'http://example.com/path/to/keyfile',
        'fingerprint': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'
    }
    rpm_key = RpmKey(module)  # Corrected this line to instantiate the class correctly
    
    # Assert that the key is imported correctly
    assert module.exit_json.called
    assert module.exit_json.call_args[1]['changed'] is True

def test_import_key_from_file(mocker, module):
    # Mock the fetch_key method to return None (since we are using a local file)
    mocker.patch('ansible.modules.rpm_key.RpmKey.fetch_key', return_value=None)
    # Initialize RpmKey with module parameters for importing a key from a local file
    module.params = {
        'state': 'present',
        'key': '/path/to/local/keyfile',
        'fingerprint': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'
    }
    rpm_key = RpmKey(module)  # Corrected this line to instantiate the class correctly
    
    # Assert that the key is imported correctly
    assert module.exit_json.called
    assert module.exit_json.call_args[1]['changed'] is True

def test_drop_existing_key(mocker, module):
    # Mock the is_key_imported method to return True (indicating the key is imported)
    mocker.patch('ansible.modules.rpm_key.RpmKey.is_key_imported', return_value=True)
    # Initialize RpmKey with module parameters for dropping a key
    module.params = {
        'state': 'absent',
        'key': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'
    }
    rpm_key = RpmKey(module)  # Corrected this line to instantiate the class correctly
    
    # Assert that the key is dropped correctly
    assert module.exit_json.called
    assert module.exit_json.call_args[1]['changed'] is True

def test_import_key_with_incorrect_fingerprint(mocker, module):
    # Mock the fetch_key method to return a temporary file path
    mocker.patch('ansible.modules.rpm_key.RpmKey.fetch_key', return_value='/tmp/keyfile')
    # Initialize RpmKey with module parameters for importing a key with an incorrect fingerprint
    module.params = {
        'state': 'present',
        'key': 'http://example.com/path/to/keyfile',
        'fingerprint': '12:34:56:78:90:12:34:56:78:90:12:34:56'  # Incorrect fingerprint
    }
    rpm_key = RpmKey(module)  # Corrected this line to instantiate the class correctly
    
    # Assert that the module fails due to incorrect fingerprint
    assert module.fail_json.called

def test_import_key_with_missing_file(mocker, module):
    # Mock the fetch_key method to return None (since the key file is missing)
    mocker.patch('ansible.modules.rpm_key.RpmKey.fetch_key', return_value=None)
    # Initialize RpmKey with module parameters for importing a non-existent key file
    module.params = {
        'state': 'present',
        'key': '/path/to/nonexistent/keyfile',
        'fingerprint': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'
    }
    rpm_key = RpmKey(module)  # Corrected this line to instantiate the class correctly
    
    # Assert that the module fails due to missing key file
    assert module.fail_json.called
