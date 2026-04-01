
import os
from contextlib import contextmanager
from isort.deprecated.finders import chdir
import pytest

@pytest.fixture(scope="module")
def valid_directory():
    # Create a temporary directory for testing
    temp_dir = "/tmp/test_chdir"
    os.makedirs(temp_dir, exist_ok=True)
    yield temp_dir
    # Clean up the temporary directory after the test
    os.rmdir(temp_dir)

def test_valid_input(valid_directory):
    with chdir(valid_directory) as cm:
        assert os.getcwd() == valid_directory
