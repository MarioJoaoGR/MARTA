
import subprocess
import pytest
from unittest.mock import patch

def get_output(command: list[str]) -> str:
    """Run a command and return raw output

    :param str command: the command to run
    :returns: the stdout output of the command
    """
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)  # nosec
    return result.stdout.decode()

@pytest.mark.parametrize("valid_command", [["ls", "-l"]])
def test_valid_input(valid_command):
    with patch('subprocess.run') as mock_run:
        expected_output = "mocked output"
        mock_run.return_value.stdout = expected_output.encode()
        
        assert get_output(valid_command) == expected_output
