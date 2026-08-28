
import pytest
from unittest.mock import patch, MagicMock
from dataclasses import dataclass

@dataclass
class KeyValueArg:
    value: str
    orig: str

def process_data_embed_file_contents_arg(arg: KeyValueArg) -> str:
    return load_text_file(arg)

def load_text_file(arg: KeyValueArg) -> str:
    try:
        with open(arg.value, 'r', encoding='utf-8' if arg.orig.endswith('.txt') else 'ascii') as file:
            return file.read()
    except FileNotFoundError:
        raise ParseError(f"File not found at {arg.orig}")
    except UnicodeDecodeError:
        raise ParseError(f"Failed to decode the content of {arg.orig} using UTF-8 or ASCII")

class ParseError(Exception):
    pass

# Test for basic functionality
def test_process_data_embed_file_contents_arg_basic():
    @dataclass
    class KeyValueArg:
        value: str
        orig: str

    # Create a valid KeyValueArg instance
    item = KeyValueArg(value='tests/test_file.txt', orig='"tests/test_file.txt"')

    # Use patch to mock the open function and ensure it reads the file correctly
    with patch('builtins.open', create=True) as mock_open:
        mock_instance = MagicMock()
        mock_instance.read.return_value = "Test content"
        mock_open.return_value.__enter__.return_value = mock_instance
        
        # Call the function and assert the result
        result = process_data_embed_file_contents_arg(item)
        assert result == "Test content"
