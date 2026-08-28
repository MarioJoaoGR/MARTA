
import pytest
from io import BytesIO

# Import the function from the module
def _s32(reader):
    v = _read_int(reader)
    if v & 0x80000000 != 0:
        v = - ((v ^ 0xffffffff) + 1)
    return v

# Mock function to simulate reading an integer from a binary stream
def _read_int(reader):
    byte_data = reader.read(4)
    if len(byte_data) < 4:
        raise EOFError("End of stream reached before reading 4 bytes")
    return int.from_bytes(byte_data, 'big', signed=True)

# Test cases for _s32 function
def test_s32_positive_integer():
    data = b'\x00\x00\x00\x7F'  # Binary representation of an integer 127
    reader = BytesIO(data)
    assert _s32(reader) == 127

def test_s32_negative_integer():
    data = b'\xFF\xFF\xFF\x80'  # Binary representation of a negative integer -128
    reader = BytesIO(data)