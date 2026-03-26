
import subprocess
import pytest
from unittest.mock import patch

def get_output(command: list[str]) -> str:
    """Run a command and return raw output"""
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)  # nosec
    return result.stdout.decode()

@pytest.mark.parametrize("command", [["ls", "-l"], ["echo", "Hello, World!"]])
def test_valid_input(command):
    with patch('subprocess.run') as mock_run:
        # Mock the subprocess.run to return a successful result with predefined stdout
        mock_result = subprocess.CompletedProcess(args=command, returncode=0, stdout="Mocked output".encode())
        mock_run.return_value = mock_result
        
        # Call the function under test
        output = get_output(command)
        
        # Assert that the mocked subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(command, stdout=subprocess.PIPE, check=True)
        
        # Assert that the output matches the expected value
        assert output == "Mocked output"
