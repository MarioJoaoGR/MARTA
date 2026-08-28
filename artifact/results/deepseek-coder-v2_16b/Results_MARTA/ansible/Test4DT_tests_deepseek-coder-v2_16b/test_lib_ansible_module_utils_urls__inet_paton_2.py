
import pytest
import socket
import sys
from unittest.mock import patch

def _inet_paton(ipname):
    """Try to convert an IP address to packed binary form

    Supports IPv4 addresses on all platforms and IPv6 on platforms with IPv6
    support.
    """
    try:
        b_ipname = to_bytes(ipname, errors='strict')
    except UnicodeError:
        raise ValueError("%s must be an all-ascii string." % repr(ipname))

    if sys.version_info < (3,):
        n_ipname = b_ipname
    else:
        n_ipname = ipname

    if n_ipname.count('.') == 3:
        try:
            return socket.inet_aton(n_ipname)
        except (OSError, socket.error, TypeError):
            pass

    try:
        return socket.inet_pton(socket.AF_INET6, n_ipname)
    except (OSError, socket.error, TypeError):
        raise ValueError("%s is neither an IPv4 nor an IP6 "
                         "address." % repr(ipname))
    except AttributeError:
        pass

    raise ValueError("%s is not an IPv4 address." % repr(ipname))

@pytest.fixture
def valid_ipv4():
    return '192.168.1.1'

@pytest.fixture
def valid_ipv6():
    return '::1'

@pytest.fixture
def invalid_input():
    return 'invalid ip address'

def test_valid_ipv4(valid_ipv4):
    result = _inet_paton(valid_ipv4)
    expected_output = b'\xc0\xa8\x01\x01'
    assert bytes(result) == expected_output

def test_valid_ipv6(valid_ipv6):
    result = _inet_paton(valid_ipv6)
    expected_output = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    assert bytes(result) == expected_output

def test_invalid_input(invalid_input):
    with pytest.raises(ValueError) as e:
        _inet_paton(invalid_input)
    assert str(e.value) == "'invalid ip address' must be an all-ascii string."
