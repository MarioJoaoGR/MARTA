
# Module: string_utils.manipulation
# test_string_utils.py
from string_utils import manipulation as sm
import pytest
import base64
import zlib

def test_decompress_basic():
    compressed = zlib.compress("Hello, World!".encode('utf-8'))
    encoded = base64.b64encode(compressed).decode('utf-8')
    assert sm.decompress(encoded) == "Hello, World!"

def test_decompress_with_specified_encoding():
    compressed = zlib.compress("Hello, World!".encode('utf-8'))
    encoded = base64.b64encode(compressed).decode('utf-8')