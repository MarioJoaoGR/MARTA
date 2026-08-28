
import pytest
import socket
import struct

def recv_data(s):
    header_len = 8  # size of a packed unsigned long long
    data = to_bytes("")
    while len(data) < header_len:
        d = s.recv(header_len - len(data))
        if not d:
            return None
        data += d
    data_len = struct.unpack('!Q', data[:header_len])[0]
    data = data[header_len:]
    while len(data) < data_len:
        d = s.recv(data_len - len(data))
        if not d:
            return None
        data += d
    return data

# Test 1: test_valid_case
def test_valid_case():
    # Create a mock socket object with recv method that returns valid data
    class MockSocket:
        def __init__(self, data):
            self.data = data
        
        def recv(self, bufsize):
            if len(self.data) > 0:
                return self.data[:bufsize]
            else:
                return b''
    
    # Create a mock socket object with valid data
    s = MockSocket(b'\x00\x00\x00\x00\x00\x00\x00\x10Hello, World!')
    
    # Call the function and check if it returns the expected data
    result = recv_data(s)
    assert result == b'Hello, World!'

# Test 2: test_missing_data
def test_missing_data():
    # Create a mock socket object that closes the connection immediately
    class MockSocket:
        def __init__(self):
            self.closed = False
        
        def recv(self, bufsize):
            if not self.closed:
                self.closed = True
                return b''
            else:
                raise ConnectionError("Connection closed")
    
    # Create a mock socket object and close it immediately
    s = MockSocket()
    
    # Call the function and check if it returns None due to missing data
    result = recv_data(s)
    assert result is None

# Test 3: test_invalid_input
def test_invalid_input():
    # Create a mock socket object with invalid input (None)
    s = None
    
    # Call the function and check if it raises TypeError due to invalid input
    with pytest.raises(TypeError):
        recv_data(s)
