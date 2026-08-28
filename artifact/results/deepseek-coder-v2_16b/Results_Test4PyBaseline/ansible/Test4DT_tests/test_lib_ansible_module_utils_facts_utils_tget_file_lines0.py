
import pytest
from ansible.module_utils.facts.utils import get_file_lines
import os

# Helper function to create a temporary file with given content for testing
def create_temp_file(content):
    with open('temp_file.txt', 'w') as f:
        f.write(content)
    return 'temp_file.txt'

@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield  # run the test cases
    if os.path.exists('temp_file.txt'):
        os.remove('temp_file.txt')

# Test cases for get_file_lines function
def test_get_file_lines_basic():
    path = create_temp_file("Line one\nLine two\nLine three")
    assert get_file_lines(path) == ['Line one', 'Line two', 'Line three']

def test_get_file_lines_strip():
    path = create_temp_file(" Line one \n Line two \n Line three ")