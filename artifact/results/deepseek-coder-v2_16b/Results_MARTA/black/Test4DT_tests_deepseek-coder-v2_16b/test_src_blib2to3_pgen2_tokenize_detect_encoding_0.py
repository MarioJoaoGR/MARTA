
import pytest
from blib2to3.pgen2.tokenize import detect_encoding
from typing import Callable, List, Tuple

# Constants for testing
VALID_INPUT = b"# coding: utf-8\nprint('Hello, World!')\n"
INVALID_INPUT = b"\xef\xbb\xbfprint('Hello, World!')\n"
NO_ENCODING_INPUT = b"print('Hello, World!')\n"


def test_valid_input_without_bom():
    def readline():
        yield b"# coding: utf-8\nprint('Hello, World!')\n"
    
    encoding, lines = detect_encoding(lambda: next(readline()))
    assert encoding == "utf-8", f"Expected 'utf-8', but got {encoding}"


def test_no_coding_cookie():
    def readline():
        yield NO_ENCODING_INPUT
    
    encoding, lines = detect_encoding(lambda: next(readline()))
    assert encoding == "utf-8", f"Expected 'utf-8', but got {encoding}"