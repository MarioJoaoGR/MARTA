
import pytest
from unittest.mock import patch
import os

def _is_key_file_encrypted(key_file):
    """Detects if a key file is encrypted or not.

    This function checks whether the specified key file is encrypted by looking for the string "ENCRYPTED" in its content. It opens the file and reads through each line to see if the string appears anywhere in the text. If it finds the string, the function returns `True`, indicating that the file is encrypted. Otherwise, it returns `False`.

    Parameters:
        key_file (str): The path to the key file you want to check for encryption status. This should be a string representing the file's location on your filesystem.

    Returns:
        bool: True if the key file is encrypted according to the presence of "ENCRYPTED" in its content, False otherwise.

    Example:
        To check if a file named 'secret_key.txt' located at '/path/to/file' is encrypted, you would call the function like this:
        
        ```python
        result = _is_key_file_encrypted('/path/to/file/secret_key.txt')
        print(result)  # This will print True if 'secret_key.txt' is encrypted, False otherwise.
        ```
    """
    with open(key_file, "r") as f:
        for line in f:
            if "ENCRYPTED" in line:
                return True
    return False

@pytest.fixture
def create_temp_key_file():
    content = 'This is a test ENCRYPTED line.'
    temp_file_path = '/tmp/test_key_file.txt'
    with open(temp_file_path, "w") as f:
        f.write(content)
    yield temp_file_path
    os.remove(temp_file_path)

def test_valid_input(create_temp_key_file):
    assert _is_key_file_encrypted(create_temp_key_file) is True
