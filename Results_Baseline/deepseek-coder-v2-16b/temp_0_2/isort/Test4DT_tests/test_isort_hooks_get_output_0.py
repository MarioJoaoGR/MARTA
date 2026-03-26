
import subprocess

import pytest

from isort.hooks import get_output


def test_get_output_basic():
    command = ['ls', '-l']
    expected_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()
    assert get_output(command) == expected_output

def test_get_output_with_arguments():
    command = ['grep', 'hello', 'file.txt']
    with pytest.raises(subprocess.CalledProcessError):
        get_output(command)

def test_get_output_with_spaces():
    command = ['echo', 'Hello World']
    expected_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()
    assert get_output(command) == expected_output
