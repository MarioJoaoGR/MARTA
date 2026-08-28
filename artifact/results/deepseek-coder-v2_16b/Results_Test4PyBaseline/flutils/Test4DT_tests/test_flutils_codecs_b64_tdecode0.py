# Module: flutils.codecs.b64
import pytest
import base64
from typing import Tuple
from flutils.codecs.b64 import decode

# Test cases for the decode function
def test_decode_basic():
    data = b'Hello, World!'
    result = decode(data)
    assert isinstance(result[0], str), "The first element should be a string"
    assert isinstance(result[1], int), "The second element should be an integer"
    assert base64.b64encode(data).decode('utf-8') == result[0], "The encoded string does not match the expected output"
    assert len(data) == result[1], "The number of bytes consumed does not match the length of the input data"

def test_decode_bytearray():
    data = bytearray([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])
    result = decode(data)
    assert isinstance(result[0], str), "The first element should be a string"
    assert isinstance(result[1], int), "The second element should be an integer"
    assert base64.b64encode(bytes(data)).decode('utf-8') == result[0], "The encoded string does not match the expected output"
    assert len(data) == result[1], "The number of bytes consumed does not match the length of the input data"

def test_decode_memoryview():
    data = memoryview(bytearray([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]))
    result = decode(data)
    assert isinstance(result[0], str), "The first element should be a string"
    assert isinstance(result[1], int), "The second element should be an integer"
    assert base64.b64encode(bytes(data)).decode('utf-8') == result[0], "The encoded string does not match the expected output"
    assert len(data) == result[1], "The number of bytes consumed does not match the length of the input data"

def test_decode_empty():
    data = b''
    result = decode(data)
    assert isinstance(result[0], str), "The first element should be a string"
    assert isinstance(result[1], int), "The second element should be an integer"
    assert base64.b64encode(data).decode('utf-8') == result[0], "The encoded string does not match the expected output"
    assert len(data) == result[1], "The number of bytes consumed does not match the length of the input data"
