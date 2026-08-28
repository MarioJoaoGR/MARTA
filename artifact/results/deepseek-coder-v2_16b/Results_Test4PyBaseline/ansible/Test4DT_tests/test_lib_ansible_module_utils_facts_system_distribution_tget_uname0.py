# Module: ansible.module_utils.facts.system.distribution
import pytest
from unittest.mock import MagicMock

# Import the function from the specified module
from ansible.module_utils.facts.system.distribution import get_uname

@pytest.fixture
def mock_module():
    # Create a mock module with run_command method
    mock = MagicMock()
    return mock

def test_get_uname_default_flags(mock_module):
    """Test the function with default flags."""
    expected_output = "Linux"  # Example output for 'uname -v'
    mock_module.run_command.return_value = (0, expected_output, "")
    
    result = get_uname(mock_module)
    assert result == expected_output

def test_get_uname_specific_flag(mock_module):
    """Test the function with a specific flag."""
    expected_output = "Linux version"  # Example output for 'uname -v'
    mock_module.run_command.return_value = (0, expected_output, "")
    
    result = get_uname(mock_module, flags='-v')
    assert result == expected_output

def test_get_uname_multiple_flags(mock_module):
    """Test the function with multiple flags."""
    expected_output = "Linux version release"  # Example output for 'uname -v -r'
    mock_module.run_command.return_value = (0, expected_output, "")
    
    result = get_uname(mock_module, flags='-v -r')
    assert result == expected_output

def test_get_uname_custom_flags(mock_module):
    """Test the function with custom flags."""
    expected_output = "Linux architecture mode"  # Example output for 'uname -m -o'
    mock_module.run_command.return_value = (0, expected_output, "")
    
    result = get_uname(mock_module, flags=['-m', '-o'])
    assert result == expected_output

def test_get_uname_invalid_flags(mock_module):
    """Test the function with invalid flags."""
    mock_module.run_command.return_value = (1, "", "Invalid flag")
    
    result = get_uname(mock_module, flags='-x')
    assert result is None

def test_get_uname_no_flags(mock_module):
    """Test the function with no flags."""
    expected_output = "Linux version"  # Example output for 'uname -v'
    mock_module.run_command.return_value = (0, expected_output, "")
    
    result = get_uname(mock_module)
    assert result == expected_output
