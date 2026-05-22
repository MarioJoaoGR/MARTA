
import pytest
from httpie.cli.argtypes import readable_file_arg

@pytest.fixture
def valid_files():
    return ['example.txt']

def test_valid_input(valid_files):
    assert readable_file_arg(valid_files[0]) == 'example.txt'
