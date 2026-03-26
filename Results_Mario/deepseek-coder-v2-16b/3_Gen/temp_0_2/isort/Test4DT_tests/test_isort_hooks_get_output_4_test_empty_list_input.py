
import subprocess
from unittest import mock
import pytest

def get_output(command: list[str]) -> str:
    """Run a command and return raw output.

    This function takes a list of strings representing a command to be executed by the system. It runs the command and captures its standard output, which is then returned as a decoded string. The function uses `subprocess.run` with specified parameters to execute the command and ensure it completes successfully before capturing the output.

    Parameters:
        command (list[str]): A list of strings representing the command to be executed. Each element in the list corresponds to a part of the command. For example, ['ls', '-l'] would run the 'ls -l' command.

    Returns:
        str: The raw stdout output of the command as a decoded string.

    Example:
        To get the output of the 'ls -l' command on Unix-like systems, you can call:
        
        >>> get_output(['ls', '-l'])
        'total 12\n-rw-r--r--  1 user group  100 Oct  1 12:34 file.txt\n...'\n

    Note:
        This function assumes that the command provided in the list is a valid command that can be executed by the system and returns its standard output. It does not handle errors or exceptions related to the command execution, such as permission issues or non-existent commands.
    """
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)  # nosec
    return result.stdout.decode()

@pytest.mark.parametrize("command, expected", [
    (['ls', '-l'], 'output of ls -l command'),
    (['echo', 'hello'], 'hello')
])
def test_get_output(command, expected):
    with mock.patch('subprocess.run', return_value=mock.Mock(stdout=expected.encode())):
        assert get_output(command) == expected
