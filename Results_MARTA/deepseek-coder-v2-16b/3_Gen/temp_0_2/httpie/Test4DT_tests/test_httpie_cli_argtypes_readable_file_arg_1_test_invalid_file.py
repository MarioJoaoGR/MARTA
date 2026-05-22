
import pytest
from unittest.mock import patch, MagicMock
import argparse

def readable_file_arg(filename):
    """
    Check if the given file is readable and return its name, or raise an error if not.

    Parameters:
        filename (str): The path to the file you want to check.

    Returns:
        str: The name of the file if it is readable.

    Raises:
        argparse.ArgumentTypeError: If the file does not exist or is not readable, an error message indicating the issue will be raised.

    Examples:
        >>> readable_file_arg('example.txt')
        'example.txt'
        
        >>> try:
        ...     print(readable_file_arg('nonexistent.txt'))
        ... except argparse.ArgumentTypeError as e:
        ...     print(e)
        nonexistent.txt: No such file or directory
    """
    try:
        with open(filename, 'rb'):
            return filename
    except OSError as ex:
        raise argparse.ArgumentTypeError(f'{ex.filename}: {ex.strerror}')

@pytest.mark.parametrize("file_path", ["nonexistent.txt"])
def test_invalid_file(file_path):
    with pytest.raises(argparse.ArgumentTypeError) as excinfo:
        readable_file_arg(file_path)
    assert str(excinfo.value) == f'{file_path}: No such file or directory'
