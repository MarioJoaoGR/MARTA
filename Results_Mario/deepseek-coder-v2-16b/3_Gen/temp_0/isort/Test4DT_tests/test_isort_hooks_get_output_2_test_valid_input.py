
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
    # Known good command
    command = ['ls', '-l']
    
    # Expected output for the 'ls -l' command on a Unix-like system
    expected_output = subprocess.run(command, stdout=subprocess.PIPE, check=True).stdout.decode()  # nosec
    
    # Actual output from the function
    actual_output = get_output(command)
    
    # Assert that the actual output matches the expected output
    assert actual_output == expected_output
