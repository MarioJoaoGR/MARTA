
# Module: ansible.modules.rpm_key
import pytest
from ansible.module_utils.basic import AnsibleModule
from unittest.mock import patch, MagicMock
import os
import tempfile
from io import BytesIO

# Mock the fetch_url function to simulate fetching a key from a URL
def mock_fetch_url(module, url):
    if 'http://example.com/path/to/keyfile' == url:
        return (BytesIO(b"mocked public key content"), {'status': 200})
    else:
        raise ValueError("Invalid URL")

# Mock the is_pubkey function to check if the fetched content is a public key
def mock_is_pubkey(content):
    return b'public key' in content

@pytest.fixture
def module():
    params = {
        'state': 'present',
        'key': 'http://example.com/path/to/keyfile',
        'fingerprint': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'
    }
    module = AnsibleModule(argument_spec={
        'state': {'type': 'str', 'default': 'present'},
        'key': {'type': 'str', 'required': True},
        'fingerprint': {'type': 'str'}
    })
    module.params = params
    return module

@pytest.fixture
def rpm_key(module):
    class RpmKey:
        def __init__(self, module):
            self.module = module
        
        def fetch_key(self, url):
            if 'http://example.com/path/to/keyfile' == url:
                return (BytesIO(b"mocked public key content"), {'status': 200})
            else:
                raise ValueError("Invalid URL")
        
        def is_pubkey(self, content):
            return b'public key' in content
    
    return RpmKey(module)

# Test importing a key from a URL
def test_import_key_from_url(module, rpm_key):
    with patch('ansible.modules.rpm_key.RpmKey.fetch_key', side_effect=mock_fetch_url), \
         patch('ansible.modules.rpm_key.RpmKey.is_pubkey', side_effect=mock_is_pubkey):
        rpm_key.__init__(module)
        assert module.params['state'] == 'present'
        assert os.path.exists(module.params['key'])
        # Add more assertions to check the key content and fingerprint if necessary

# Test importing a key from a local file
def test_import_key_from_local_file(module, rpm_key):
    module.params['key'] = '/path/to/local/keyfile'  # Update the key parameter to point to a local file
    with patch('ansible.modules.rpm_key.RpmKey.is_pubkey', side_effect=mock_is_pubkey):
        rpm_key.__init__(module)
        assert module.params['state'] == 'present'
        # Add more assertions to check the key content and fingerprint if necessary

# Test dropping an existing key
def test_drop_existing_key(module, rpm_key):
    with patch('ansible.modules.rpm_key.RpmKey.is_key_imported', return_value=True):
        rpm_key.__init__(module)
        assert module.params['state'] == 'absent'
        # Add more assertions to check the key removal if necessary

# Test handling a non-public key URL
def test_non_public_key_url(module, rpm_key):
    with patch('ansible.modules.rpm_key.RpmKey.fetch_key', side_effect=ValueError("Not a public key")), \
         pytest.raises(SystemExit) as excinfo:
        rpm_key.__init__(module)
        assert "Not a public key" in str(excinfo.value)
