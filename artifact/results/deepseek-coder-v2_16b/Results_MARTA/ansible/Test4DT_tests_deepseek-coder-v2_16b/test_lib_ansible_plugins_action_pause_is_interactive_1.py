
import pytest
from unittest.mock import patch
from os import tty_get, getpgrp, tcgetpgrp

def is_interactive(fd=None):
    if fd is None:
        return False

    if isatty(fd):
        # Compare the current process group to the process group associated
        # with terminal of the given file descriptor to determine if the process
        # is running in the background.
        return getpgrp() == tcgetpgrp(fd)
    else:
        return False

@pytest.mark.parametrize("fd, expected", [
    (0, False),  # Standard input should not be interactive
    (None, False),  # Default to file descriptor 0 if no specific fd is provided
])
def test_valid_case_standard_input(fd, expected):
    assert is_interactive(fd) == expected

@pytest.mark.parametrize("arg, expected", [
    (None, False),  # None should default to checking file descriptor 0
])
def test_edge_case_none(arg, expected):
    with patch('os.isatty', return_value=False):  # Mock isatty to always return False for non-terminal checks
        assert is_interactive(arg) == expected

@pytest.mark.parametrize("fd", [999])  # Non-existent or non-terminal file descriptor
def test_error_case_invalid_fd(fd):
    with pytest.raises(OSError), patch('os.isatty', return_value=False), patch('os.getpgrp', side_effect=Exception("Process group not available")):
        assert is_interactive(fd) == False  # This should raise an error and fail the test if it doesn't
