
import pytest
from unittest.mock import patch, MagicMock
import os

def _is_key_file_encrypted(key_file):
    """Detects if a key file is encrypted or not.

    This function checks whether the specified key file is encrypted by looking for the string "ENCRYPTED" in its content. It opens the file and reads through each line to see if the string appears anywhere in the text. If it finds the string, the function returns `True`, indicating that the file is encrypted. Otherwise, it returns `False`.

    Parameters:
        key_file (str): The path to the key file you want to check for encryption status. This should be a string representing the file's location on your filesystem.

    Returns:
        bool: True if the key file is encrypted according to the presence of "ENCRYPTED" in its content, False otherwise.
    """
    with open(key_file, "r") as f:
        for line in f:
            # Look for Proc-Type: 4,ENCRYPTED
            if "ENCRYPTED" in line:
                return True

    return False

@pytest.fixture
def create_empty_file(tmpdir):
    empty_file = tmpdir.join("empty_key_file.txt")
    empty_file.write("")
    return str(empty_file)

def test_empty_file(create_empty_file):
    assert not _is_key_file_encrypted(create_empty_file)
