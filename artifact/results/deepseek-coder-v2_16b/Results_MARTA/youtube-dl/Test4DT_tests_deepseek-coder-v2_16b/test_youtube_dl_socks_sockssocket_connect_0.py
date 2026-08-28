
import pytest
from youtube_dl.socks import sockssocket
import socket


def test_invalid_address_format():
    sock = sockssocket()
    with pytest.raises(TypeError):
        sock.connect(("invalid-host", "invalid-port"))
