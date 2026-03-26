
import pytest
from unittest.mock import patch, MagicMock
import typing as T

# Assuming the global list 'parts' is defined somewhere in your codebase
parts = []

def process_one(arg):
    raise TypeError("Invalid argument type")

def process_sect(name: str, args: T.List[T.Any]):
    if args:
        parts.append(name)
        for arg in args:
            process_one(arg)
        parts.append("")

# Test function to test invalid input with non-string section name and list of non-processable arguments
@pytest.mark.parametrize("name, args", [
    (123, ["test"]),  # Non-string section name
    ("section_name", [123]),  # List containing a non-processable argument
])
def test_invalid_input(name, args):
    with pytest.raises(TypeError):
        process_sect(name, args)
