
import pytest
from ansible.plugins.action import include_vars

@pytest.fixture(scope="module")
def action_module():
    return include_vars.ActionModule()

# Test for valid YAML file
def test_valid_case_yaml(action_module):
    filename = 'path/to/example.yaml'
    result = action_module._load_files(filename, validate_extensions=True)
    assert not result[0], "Expected successful loading of a valid YAML file"
    assert isinstance(result[2], dict), "Loaded content must be a dictionary"

# Test for invalid extension file
def test_error_case_invalid_extension(action_module):
    filename = 'path/to/unknown_file'
    result = action_module._load_files(filename, validate_extensions=True)
    assert result[0], "Expected failure due to invalid extension"
    assert "does not have a valid extension" in result[1].lower(), f"Error message should indicate invalid extension: {result[1]}"

# Test for nonexistent file
def test_error_case_nonexistent_file(action_module):
    filename = 'non_existent_file'
    result = action_module._load_files(filename, validate_extensions=False)
    assert result[0], "Expected failure due to nonexistent file"
    assert "No such file or directory" in result[1].lower(), f"Error message should indicate the file does not exist: {result[1]}"
