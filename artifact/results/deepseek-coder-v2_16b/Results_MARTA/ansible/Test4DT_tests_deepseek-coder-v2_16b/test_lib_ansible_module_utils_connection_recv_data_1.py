
import pytest
from ansible.module_utils.connection import recv_data
from unittest.mock import MagicMock
import struct


def test_recv_data_no_data():
    mock_socket = MagicMock()
    mock_socket.recv.side_effect = [b'', '']
    assert recv_data(mock_socket) is None
