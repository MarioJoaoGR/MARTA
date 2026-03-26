
import tokenize
from io import TextIOBase
from pathlib import Path
from typing import Callable, TextIO

import pytest

from isort.exceptions import UnsupportedEncoding
from isort.io import File


# Mock the necessary parts of the tokenize module for testing purposes
class MockTokenize:
    @staticmethod
    def detect_encoding(readline: Callable[[], bytes]) -> tuple[str, dict]:
        # This mock will always return 'utf-8' encoding
        return ('utf-8', {})

# Replace the actual tokenize module with our mock
tokenize.detect_encoding = MockTokenize.detect_encoding

@pytest.fixture
def file():
    stream = TextIOBase()  # A mock for a text stream
    path = Path("example_file.txt")  # The path to the file
    encoding = "utf-8"  # The assumed encoding of the file
    return File(stream, path, encoding)

def test_detect_encoding_with_string_filename_and_generator(tmp_path):
    filename = tmp_path / "example_file.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("test content")
    
    def readline():
        yield b"test content\n"
    
    detected_encoding = File.detect_encoding(str(filename), readline)
    assert detected_encoding == 'utf-8'

def test_detect_encoding_with_path_object_and_generator(tmp_path):
    filename = tmp_path / "example_file.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("test content")
    
    def readline():
        yield b"test content\n"
    
    detected_encoding = File.detect_encoding(filename, readline)
    assert detected_encoding == 'utf-8'

def test_detect_encoding_with_string_filename_and_builtin_readline(tmp_path):
    filename = tmp_path / "example_file.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("test content")
    
    detected_encoding = File.detect_encoding(str(filename), open(filename, "rb").readline)
    assert detected_encoding == 'utf-8'

def test_detect_encoding_with_path_object_and_builtin_readline(tmp_path):
    filename = tmp_path / "example_file.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("test content")
    
    detected_encoding = File.detect_encoding(filename, open(filename, "rb").readline)