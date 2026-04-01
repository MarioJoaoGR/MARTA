
import subprocess
import pytest

def get_lines(command: list[str]) -> list[str]:
    """Run a command and return lines of output.

    This function takes a list of strings representing a command to be executed by the system. It runs the command and captures its standard output, which is then returned as a list of whitespace-stripped lines. The function uses subprocess module to execute the command.

    Parameters:
        command (list[str]): A list of strings where each element is a part of the command to run. For example, ['ls', '-l'] would run the 'ls -l' command.

    Returns:
        list[str]: A list of whitespace-stripped lines from the command output.

    Example:
        To get the lines of output for the 'ls -l' command, you can call:
        
        >>> get_lines(['ls', '-l'])
        ['total 12', '-rw-r--r--  1 user group  1024 Jan  1 12:34 file.txt', ...]
    """
    stdout = subprocess.run(command, capture_output=True, text=True)
    return [line.strip() for line in stdout.stdout.splitlines()]

# Test case for get_lines function with None input
def test_none_input():
    with pytest.raises(TypeError):
        assert get_lines(None) == []
