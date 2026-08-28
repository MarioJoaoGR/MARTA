
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.socks import sockssocket, ProxyType

def test_sockssocket_init_without_parameters():
    with patch('youtube_dl.socks.socket') as mock_socket:
        sock = sockssocket()
        assert sock._proxy is None
        mock_socket.assert_not_called()


