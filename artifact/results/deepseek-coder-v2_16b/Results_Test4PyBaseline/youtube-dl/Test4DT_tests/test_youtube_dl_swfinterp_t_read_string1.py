
import pytest
from io import BytesIO
import struct  # Importing the struct module as it was intended but not used correctly in the original code.

# Helper function to read a string from a reader (assuming it's defined elsewhere)
def _read_string(reader):
    slen = _u30(reader)
    resb = reader.read(slen)
    assert len(resb) == slen, f"Expected length {slen}, but got {len(resb)}"
    return resb.decode('utf-8')

# Helper function to test the _u30 function (assuming it's defined elsewhere)
def _u30(reader):
    data = b''
    for _ in range(4):
        byte = reader.read(1)
        if not byte:
            raise ValueError("Unexpected end of stream")
        data += byte
    return struct.unpack('>I', data)[0]  # Correctly using the struct module here.

# Test cases for the _read_string function
def test_read_string_valid():
    # Create a BytesIO object with valid data
    data = b'\x04' + b'hello'  # A 32-bit unsigned integer (4) followed by the UTF-8 encoded string 'hello'
    reader = BytesIO(data)
    
    # Call the function and check the result