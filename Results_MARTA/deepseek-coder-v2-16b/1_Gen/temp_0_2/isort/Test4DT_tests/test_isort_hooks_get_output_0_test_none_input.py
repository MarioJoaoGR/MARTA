
import subprocess
import pytest
from unittest.mock import patch

def get_output(command: list[str]) -> str:
    """Run a command and return raw output.

    This function takes a list of strings representing a command to be executed by the system. It runs the command and captures its standard output, which is then returned as a decoded string. The function uses `subprocess.run` with specified parameters to execute the command and ensure it completes successfully before returning the output.

    Parameters:
        command (list[str]): A list of strings representing the command to be executed. Each element in the list corresponds to a part of the command. For example, ['ls', '-l'] would run 'ls -l' on Unix-like systems.

    Returns:
        str: The standard output of the command as a decoded string.

    Example:
        To get the raw output of the command that lists files in the current directory, you can use:
        
        >>> get_output(['ls', '-l'])
        'total 12\n-rw-r--r--  1 user group  100 Jan 1 12:34 file1.txt\n...'\n
    """
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)  # nosec
    return result.stdout.decode()

def test_none_input():
    with pytest.raises(TypeError):
        get_output(None)
