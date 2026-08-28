
import pytest
from ansible.modules.debconf import get_selections
from unittest.mock import MagicMock

# Mock AnsibleModule for testing
@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/debconf-show'
    return module

def test_get_selections_success(mock_module):
    # Mock the output of debconf-show for a package
    mock_module.run_command.return_value = (0, "example_key: example_value\nanother_key: another_value", "")
    
    selections = get_selections(mock_module, 'example_package')
    
    assert selections == {'example_key': 'example_value', 'another_key': 'another_value'}

def test_get_selections_failure(mock_module):
    # Mock the output of debconf-show to simulate a failure
    mock_module.run_command.return_value = (1, "", "Error retrieving selections")
    
    with pytest.raises(SystemExit) as excinfo:
        get_selections(mock_module, 'example_package')
    
    assert str(excinfo.value) == "Error retrieving selections"

def test_get_selections_empty_output(mock_module):
    # Mock the output of debconf-show to be empty
    mock_module.run_command.return_value = (0, "", "")
    
    selections = get_selections(mock_module, 'example_package')
    
    assert selections == {}

def test_get_selections_whitespace(mock_module):
    # Mock the output of debconf-show with whitespace
    mock_module.run_command.return_value = (0, " key1: value1 \n key2: value2 ", "")
    
    selections = get_selections(mock_module, 'example_package')
    
    assert selections == {'key1': 'value1', 'key2': 'value2'}
