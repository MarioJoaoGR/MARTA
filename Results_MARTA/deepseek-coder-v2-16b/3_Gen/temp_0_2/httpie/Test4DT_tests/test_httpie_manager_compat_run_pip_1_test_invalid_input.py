
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.compat import run_pip

def test_run_pip():
    # Define a mock argument list for testing
    args = ['install', 'pytest']
    
    with patch('httpie.manager.compat.is_frozen', return_value=False):
        with patch('httpie.manager.compat._discover_system_pip') as mock_discover:
            # Mock the _run_pip_subprocess to return a predefined output for testing
            mock_discover.return_value = 'mocked_pip_executable'
            
            # Run the function and capture the result
            with patch('httpie.manager.compat._run_pip_subprocess', MagicMock(side_effect=FileNotFoundError("No such file or directory"))):
                with pytest.raises(FileNotFoundError):
                    run_pip(args)
