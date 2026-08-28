
import pytest
from ansible.plugins.action.pause import is_interactive
import os

def test_is_interactive_default():
    assert not is_interactive()

def test_is_interactive_with_file_descriptor():
    # Open a file descriptor for reading (e.g., /dev/null or similar)
    fd = open(os.devnull, 'r')
    assert not is_interactive(fd.fileno())
    fd.close()
