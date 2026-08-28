
import pytest
from apimd.loader import _load_module
from apimd.parser import Parser


def test_nonexistent_file():
    parser = Parser()
    result = _load_module('nonexistent_module', 'nonexistent_module.py', parser)
    assert not result, "Expected False for nonexistent file"


def test_valid_extension_module():
    # Create a mock .so file for testing purposes
    with open('test_module.so', 'wb') as f:
        f.write(b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00>\x00\x01\x00\x00\x00\x80@\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00')
    
    parser = Parser()
    result = _load_module('test_module', 'test_module.so', parser)
    assert not result, "Expected False for invalid extension module content"

def test_empty_extension_module():
    # Create an empty .so file for testing purposes
    with open('empty_module.so', 'wb') as f:
        pass  # Empty file to simulate a compiled extension
    
    parser = Parser()
    result = _load_module('empty_module', 'empty_module.so', parser)
    assert not result, "Expected False for empty extension module"