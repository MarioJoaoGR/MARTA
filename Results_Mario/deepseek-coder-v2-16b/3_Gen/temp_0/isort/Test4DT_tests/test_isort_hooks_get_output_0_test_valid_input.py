
import subprocess

import pytest


def get_output(command: list[str]) -> str:
    """Run a command and return raw output

    :param str command: the command to run
    :returns: the stdout output of the command
    """
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)  # nosec
    return result.stdout.decode()

def test_valid_input():
    # Known good command to test with
    command = ['ls', '-l']
    
    # Expected output for the 'ls -l' command on a Unix-like system
    expected_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()  # nosec
    
    # Run the function and assert that it returns the expected output
    assert get_output(command) == expected_output
