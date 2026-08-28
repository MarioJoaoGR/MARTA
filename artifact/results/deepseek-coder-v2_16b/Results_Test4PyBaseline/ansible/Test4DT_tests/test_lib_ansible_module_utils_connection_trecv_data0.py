
import pytest
from unittest.mock import MagicMock
import struct

# Assuming the function is defined in a module named ansible.module_utils.connection
from ansible.module_utils.connection import recv_data

def test_recv_data_with_valid_socket():
    # Create a mock socket with some predefined data to be received
    mock_socket = MagicMock()
    expected_data = b'example data'
    header_len = 8
    total_data_length = len(expected_data)
    
    # Simulate the socket receiving the header first, then the rest of the data
    mock_socket.recv.side_effect = [struct.pack('!Q', total_data_length)[:header_len], expected_data]
    
    # Call the function with the mock socket
    received_data = recv_data(mock_socket)
    
    # Assert that the correct data was received and returned
    assert received_data == expected_data
    # Ensure the socket's recv method was called as expected
    assert mock_socket.recv.call_count == 2

def test_recv_data_with_empty_socket():
    # Create a mock socket that doesn't receive any data initially
    mock_socket = MagicMock()
    mock_socket.recv.side_effect = [b'', b'', b'']
    
    # Call the function with the mock socket
    received_data = recv_data(mock_socket)
    
    # Assert that no data was received and None is returned
    assert received_data is None
    # Ensure the socket's recv method was called as expected