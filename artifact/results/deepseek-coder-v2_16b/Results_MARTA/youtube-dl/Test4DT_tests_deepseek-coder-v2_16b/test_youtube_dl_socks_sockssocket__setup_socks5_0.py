
import pytest
from youtube_dl.socks import sockssocket

def test_sockssocket_set_up_socks5_proxy():
    sock = sockssocket()
    with pytest.raises(TypeError):
        sock.setproxy('127.0.0.1')

def test_sockssocket_connect_via_socks5_proxy():
    sock = sockssocket()
    with pytest.raises(TypeError):
        sock.setproxy('127.0.0.1')
