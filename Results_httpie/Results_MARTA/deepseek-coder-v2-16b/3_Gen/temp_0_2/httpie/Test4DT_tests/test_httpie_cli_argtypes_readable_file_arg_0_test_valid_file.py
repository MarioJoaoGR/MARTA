
import pytest
from httpie.cli.argtypes import readable_file_arg
import os
import argparse

def test_valid_file():
    # Test with a valid file path
    valid_file = 'example.txt'
    assert readable_file_arg(valid_file) == valid_file

    # Test with an invalid file path
    invalid_file = 'nonexistent.txt'
    with pytest.raises(argparse.ArgumentTypeError) as excinfo:
        readable_file_arg(invalid_file)
    assert str(excinfo.value) == f'{invalid_file}: No such file or directory'
