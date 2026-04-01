
import pytest
from pathlib import Path
from io import TextIOWrapper
from isort.io import File

@pytest.fixture
def valid_file():
    # Create a temporary file with some content for testing
    temp_file = Path("valid_file.txt")
    temp_file.write_text("Test content", encoding="utf-8")
    yield temp_file
    # Clean up the temporary file after the test
    temp_file.unlink()

def test_valid_input(valid_file):
    file = File._open(valid_file)
    assert isinstance(file, TextIOWrapper)
    assert file.mode == "r"
    content = file.read()
    assert content == "Test content"
