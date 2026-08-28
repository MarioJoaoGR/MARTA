
# Module: ansible.modules.rpm_key
# test_rpm_key.py
from ansible.module_utils.basic import AnsibleModule
import pytest
import subprocess
import os

class RpmKey:
    def __init__(self, module):
        self.module = module
    
    def is_key_imported(self, keyid):
        cmd = f'/usr/bin/rpm -q gpg-pubkey --with-sig'
        rc, stdout, stderr = self.module.run_command(cmd)
        if 'gpg-pubkey-' + keyid in stdout:
            return True
        return False

@pytest.fixture
def module():
    class MockModule:
        def __init__(self, params):
            self.params = params
        
        def get_bin_path(self, bin_name, required=False):
            if bin_name == 'rpm':
                return '/usr/bin/rpm'
            elif bin_name == 'gpg' or bin_name == 'gpg2':
                return '/usr/bin/gpg'
            return None
        
        def run_command(self, cmd):
            if 'gpg-pubkey' in cmd:
                return 0, "Key ID: keyid\nDescription: Key description", ""
            elif 'rpm -q gpg-pubkey' in cmd:
                return 0, "gpg-pubkey-1234567890abcdef", ""
            return 1, "", "Command failed"
        
        def cleanup(self, keyfile):
            os.remove(keyfile)
    
    return MockModule({'state': 'present', 'key': 'http://example.com/path/to/keyfile', 'fingerprint': 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'})

@pytest.fixture
def rpm_key(module):
    return RpmKey(module)

def test_import_key_from_url(rpm_key, module):
    with pytest.raises(SystemExit) as e:
        rpm_key.__init__(module)
    assert str(e.value) == "0"  # Ensure the script exits cleanly

def test_is_key_imported_true(rpm_key, module):
    keyid = 'AB:CD:EF:12:34:56:78:90:12:34:56:78:90:12:34:56'
    assert rpm_key.is_key_imported(keyid) == True

def test_is_key_imported_false(rpm_key, module):
    keyid = 'GH:IJ:KL:12:34:56:78:90:12:34:56:78:90:12:34:56'
    assert rpm_key.is_key_imported(keyid) == False

def test_execute_command_success(rpm_key, module):
    cmd = '/usr/bin/rpm -q  gpg-pubkey'
    rc, stdout, stderr = module.run_command(cmd)
    assert rc == 0
    assert stdout.strip() == "gpg-pubkey-1234567890abcdef"

def test_execute_command_failure(rpm_key, module):
    cmd = 'non-existent-command'
    with pytest.raises(subprocess.CalledProcessError) as e:
        module.run_command(cmd)
    assert str(e.value) == "Command failed"
