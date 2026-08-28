# Module: ansible.plugins.action.include_vars
import pytest
from ansible.plugins.action import ActionModule

# Instantiate the ActionModule class for testing
@pytest.fixture
def action_module():
    return ActionModule()

# Test cases for _load_files method
class TestActionModuleLoadFiles:
    
    def test_valid_yaml_file(self, action_module):
        # Test loading a valid YAML file
        result = action_module._load_files('example.yaml')
        assert not result[0], "Expected operation to be successful"
        assert isinstance(result[2], dict), "Expected the content to be converted into a dictionary"
    
    def test_invalid_file_extension(self, action_module):
        # Test loading a file with an invalid extension
        result = action_module._load_files('example.txt', validate_extensions=True)
        assert result[0], "Expected operation to fail due to invalid extension"
        assert 'does not have a valid extension' in result[1], "Error message should indicate the file extension is invalid"
    
    def test_non_existent_file(self, action_module):
        # Test loading a non-existent file
        result = action_module._load_files('nonexistent.yaml')
        assert result[0], "Expected operation to fail due to the file not existing"
        assert 'No such file or directory' in result[1], "Error message should indicate that the file does not exist"
    
    def test_invalid_file_content(self, action_module):
        # Test loading a file with invalid content type
        with open('invalid_content.txt', 'w') as f:
            f.write('not valid json or yaml')
        result = action_module._load_files('invalid_content.txt')
        assert result[0], "Expected operation to fail due to invalid content"
        assert 'must be stored as a dictionary/hash' in result[1], "Error message should indicate that the content is not a valid dictionary or hash"
    
    def test_validate_extensions_false(self, action_module):
        # Test loading a file without validating extensions
        result = action_module._load_files('example.yaml', validate_extensions=False)
        assert not result[0], "Expected operation to be successful when validation is disabled"
        assert isinstance(result[2], dict), "Expected the content to be converted into a dictionary even without extension validation"
