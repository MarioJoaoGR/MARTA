
import pytest
from youtube_dl.socks import sockssocket, ProxyType




def test_connect_via_socks4_proxy():
    sock = sockssocket()
    sock.setproxy(ProxyType.SOCKS4, '127.0.0.1', 9050)
    with pytest.raises(Exception):
        sock.connect(('8.8.8.8', 53))

def test_connect_via_socks5_proxy():
    sock = sockssocket()
    sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', 9050)
    with pytest.raises(Exception):
        sock.connect(('8.8.8.8', 53))