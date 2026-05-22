
import pytest
from httpie.cli.argtypes import readable_file_arg
import os
import argparse

@pytest.fixture
def valid_files():
    # Create a temporary file for testing
    with open('temp_test_file.txt', 'w') as f:
        f.write("Test content")
    yield ['temp_test_file.txt']
    os.remove('temp_test_file.txt')

def test_valid_input(valid_files):
    filename = valid_files[0]
    assert readable_file_arg(filename) == filename
