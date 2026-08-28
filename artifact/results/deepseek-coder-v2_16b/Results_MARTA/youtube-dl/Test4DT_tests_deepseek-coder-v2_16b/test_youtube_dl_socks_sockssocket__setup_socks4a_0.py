
import pytest
from youtube_dl.socks import sockssocket
import socket


def test_sockssocket_setup_socks4a_with_proxy():
    sock = sockssocket()
    with pytest.raises(TypeError):
        sock.setproxy('192.168.1.100', 9050)