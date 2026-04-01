
import pytest
from subprocess import CalledProcessError
from unittest.mock import patch, MagicMock

def get_lines(command: list[str]) -> list[str]:
    """Run a command and return lines of output

    :param str command: the command to run
    :returns: list of whitespace-stripped lines output by command
    """
    stdout = get_output(command)
    return [line.strip() for line in stdout.splitlines()]

def get_output(command: list[str]) -> str:
    # Mock implementation for testing purposes
    raise CalledProcessError(1, ' '.join(command))

@patch('subprocess.run', side_effect=get_output)
def test_invalid_command(mock_run):
    with pytest.raises(CalledProcessError):
        get_lines(['nonexistent', '-a'])
