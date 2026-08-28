
import pytest
from flutils.pathutils import directory_present
import os
import pwd
import getpass

# Test for ensuring a directory exists at a given path

# Test for creating a new directory when the path does not exist

# Test for ensuring a directory exists with specific mode, user, and group

# Test for ensuring a directory exists with invalid path containing glob patterns
def test_invalid_path_with_glob():
    with pytest.raises(ValueError):
        # Attempt to create a directory with a glob pattern in the name, which should raise ValueError
        directory_present('*invalid')

# Test for ensuring a directory exists with non-absolute path