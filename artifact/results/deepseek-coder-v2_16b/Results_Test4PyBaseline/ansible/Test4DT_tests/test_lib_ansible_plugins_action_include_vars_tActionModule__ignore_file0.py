
# Module: ansible.plugins.action.include_vars
import pytest
from ansible.errors import AnsibleError
import re  # Importing re for regular expression operations

# Assuming action_module is an instance of ActionModule with appropriate configurations
@pytest.fixture
def action_module():
    # Create a mock ActionModule for testing
    class MockActionModule:
        TRANSFERS_FILES = False
        VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
        VALID_DIR_ARGUMENTS = ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
        VALID_FILE_ARGUMENTS = ['file', '_raw_params']
        VALID_ALL = ['name', 'hash_behaviour']
        
        def _ignore_file(self, filename):
            for file_type in self.ignore_files:
                try:
                    if re.search(r'{0}$'.format(file_type), filename):
                        return True
                except Exception:
                    err_msg = 'Invalid regular expression: {0}'.format(file_type)
                    raise AnsibleError(err_msg)
            return False
    
    # Mock ignore_files for testing purposes
    mock_action_module = MockActionModule()
    mock_action_module.ignore_files = [r'\.yaml$']  # Example pattern to match .yaml files
    return mock_action_module

# Test cases for _ignore_file method
def test_ignore_file_known_extension(action_module):
    filename = 'example.yaml'
    assert action_module._ignore_file(filename) is True

def test_ignore_file_unknown_extension(action_module):
    filename = 'unknown_extension_file'
    assert action_module._ignore_file(filename) is False

def test_ignore_file_invalid_regex(action_module):
    filename = 'invalid_pattern'
    with pytest.raises(AnsibleError, match=r'Invalid regular expression: invalid_pattern'):
        action_module._ignore_file(filename)
