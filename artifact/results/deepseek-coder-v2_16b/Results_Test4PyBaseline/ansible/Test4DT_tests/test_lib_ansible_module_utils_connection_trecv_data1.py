
import pytest
from unittest.mock import MagicMock
import struct
from ansible.module_utils.connection import recv_data

def test_recv_data_with_partial_header():
    mock_socket = MagicMock()
    header_len = 8
    partial_header = struct.pack('!Q', 1024)[:header_len // 2]
    mock_socket.recv.side_effect = [partial_header, b'']
    
    received_data = recv_data(mock_socket)
    
    assert received_data is None
    assert mock_socket.recv.call_count == 2

def test_recv_data_with_large_data():
    mock_socket = MagicMock()
    header_len = 8
    large_data = b'x' * (1024 * 1024)  # 1MB of data
    full_header = struct.pack('!Q', len(large_data))
    mock_socket.recv.side_effect = [full_header, large_data]
    
    received_data = recv_data(mock_socket)
    
    assert received_data == large_data
    assert mock_socket.recv.call_count == 2

def test_recv_data_with_no_data():
    mock_socket = MagicMock()
    mock_socket.recv.side_effect = [b'', b'']
    
    received_data = recv_data(mock_socket)
    
    assert received_data is None