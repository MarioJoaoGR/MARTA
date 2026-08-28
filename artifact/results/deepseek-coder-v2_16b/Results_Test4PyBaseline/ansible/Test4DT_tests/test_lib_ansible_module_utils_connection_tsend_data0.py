
import pytest
import socket
import pickle
import struct
from unittest.mock import patch, MagicMock

# Import the function from the module
from ansible.module_utils.connection import send_data

@patch('ansible.module_utils.connection.struct')
@patch('ansible.module_utils.connection.pickle')
@patch('ansible.module_utils.connection.socket')
def test_send_data(mock_socket, mock_pickle, mock_struct):
    # Mock the data to be sent
    data = b'{"key": "value"}'
    
    # Mock the pickle.dumps method to return the serialized data
    mock_pickle.dumps.return_value = data
    
    # Create a mock socket object with sendall method
    mock_sock = MagicMock()
    mock_socket.socket.return_value = mock_sock
    
    # Mock the struct.pack method to return the packed length
    mock_struct.pack.return_value = b'\x00\x00\x00\x00\x00\x00\x00\x10'  # Assuming len(data) is 16
    
    # Call the function with the mock socket and data
    result = send_data(mock_sock, {"key": "value"})
    
    # Assert that struct.pack was called with the correct format and length
    mock_struct.pack.assert_called_with('!Q', len(data))
    
    # Assert that pickle.dumps was called with the data
    mock_pickle.dumps.assert_called_with({"key": "value"})
    
    # Assert that sendall was called with the correct bytes
    expected_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x10' + data
    mock_sock.sendall.assert_called_with(expected_bytes)
    
    # Assert that the function returns the number of bytes sent
    assert result == len(expected_bytes)

# Add more test cases to cover different scenarios and edge cases
def test_send_data_with_empty_data():
    mock_sock = MagicMock()
    result = send_data(mock_sock, {})
    expected_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00' + pickle.dumps({})
    mock_sock.sendall.assert_called_with(expected_bytes)
    assert result == len(expected_bytes)

def test_send_data_with_large_data():
    large_data = b'a' * 1024*1024  # 1MB of data
    mock_sock = MagicMock()
    result = send_data(mock_sock, {"key": "value", "large_data": large_data})
    expected_bytes = struct.pack('!Q', len(pickle.dumps({"key": "value", "large_data": large_data}))) + pickle.dumps({"key": "value", "large_data": large_data})
    mock_sock.sendall.assert_called_with(expected_bytes)
    assert result == len(expected_bytes)
