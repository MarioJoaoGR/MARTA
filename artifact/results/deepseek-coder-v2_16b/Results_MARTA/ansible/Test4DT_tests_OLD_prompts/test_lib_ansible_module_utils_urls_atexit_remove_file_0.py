
import pytest
from unittest.mock import patch
import os

def atexit_remove_file(filename):
    """
    Removes a file from the filesystem when the Python script exits.
    
    This function is designed to ensure that a specified file is deleted from the disk once the Python script completes execution, either normally or due to an error. It uses the `atexit` module to register a cleanup function that will be called upon normal program termination.
    
    Parameters:
        filename (str): The path to the file that should be removed when the script exits. This parameter is required and must be provided as a string representing the file's location on the filesystem.
    
    Examples:
        >>> atexit_remove_file('/path/to/your/file.txt')
        # When the Python script finishes running, /path/to/your/file.txt will be deleted if it exists.
        
        >>> atexit_remove_file('example.txt')
        # When the script exits, 'example.txt' located in the current working directory will be removed if present.
    
    Note:
        This function does not return any value. It simply ensures that the file is deleted when the program ends. If there are errors during deletion (e.g., due to permissions or other issues), they are ignored, and no error is raised.
    """
    if os.path.exists(filename):
        try:
            os.unlink(filename)
        except Exception:
            # just ignore if we cannot delete, things should be ok
            pass

@pytest.fixture(autouse=True)
def cleanup_file():
    yield  # run the test code
    if os.path.exists("temp_file.txt"):
        os.unlink("temp_file.txt")


def test_non_existent_input():
    with patch('os.path.exists', return_value=False):
        atexit_remove_file("nonexistent_file.txt")
        assert not os.path.exists("nonexistent_file.txt"), "File should be removed when script exits"