
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.compat import run_pip

def test_valid_input():
    args = ['install', 'numpy']
    expected_output = b'Mocked output from pip install numpy'
    
    # Mock the subprocess call to return the expected output
    with patch('subprocess.run', return_value=MagicMock(stdout=expected_output)):
        result = run_pip(args)
        
        assert result == expected_output
