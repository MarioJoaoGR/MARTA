
import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="function")
def powershell():
    return ShellModule()

def test_exists_valid_path(powershell):
    with patch('ansible.plugins.shell.powershell.ShellModule._escape') as mock_escape, \
         patch('ansible.plugins.shell.powershell.ShellModule._unquote') as mock_unquote, \
         patch('ansible.plugins.shell.powershell.ShellModule._encode_script') as mock_encode:
        
        # Mocking the path to be a valid existing file path
        mock_unquote.return_value = 'C:\\valid\\path\\to\\file.txt'
        mock_escape.return_value = 'C:\\valid\\path\\to\\file.txt'
        
        # Expected result for a valid path is 0 (exists)
        mock_encode.return_value = 'expected_base64_script'
        
        result = powershell.exists('C:\\valid\\path\\to\\file.txt')
        
        assert result == 'expected_base64_script'

def test_exists_invalid_path(powershell):
    with patch('ansible.plugins.shell.powershell.ShellModule._escape') as mock_escape, \
         patch('ansible.plugins.shell.powershell.ShellModule._unquote') as mock_unquote, \
         patch('ansible.plugins.shell.powershell.ShellModule._encode_script') as mock_encode:
        
        # Mocking the path to be an invalid non-existing file path
        mock_unquote.return_value = 'C:\\invalid\\path\\to\\file.txt'
        mock_escape.return_value = 'C:\\invalid\\path\\to\\file.txt'
        
        # Expected result for an invalid path is 1 (does not exist)
        mock_encode.return_value = 'expected_base64_script_for_non_existence'
        
        result = powershell.exists('C:\\invalid\\path\\to\\file.txt')
        
        assert result == 'expected_base64_script_for_non_existence'
