
import pytest
from unittest.mock import patch
from mimesis.providers.internet import Internet
from ipaddress import IPv4Address



def test_invalid_input():
    internet = Internet()
    with pytest.raises(TypeError):
        internet.ip_v4(with_port=True, port_range='invalid')