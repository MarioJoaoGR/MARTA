
import pytest
import socket
import sys
from ansible.module_utils.urls import to_bytes

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

def test_valid_ipv4():
    setup_valid_ipv4 = '192.168.1.1'
    result = _inet_paton(setup_valid_ipv4)
    assert isinstance(result, bytes), "Expected a byte object for valid IPv4 address"
    assert len(result) == 4, "Expected length of 4 bytes for an IPv4 address"

def test_valid_ipv6():
    setup_valid_ipv6 = '::1'
    result = _inet_paton(setup_valid_ipv6)
    assert isinstance(result, bytes), "Expected a byte object for valid IPv6 address"
    assert len(result) == 16, "Expected length of 16 bytes for an IPv6 address"

def test_invalid_ip():
    setup_invalid_ip = 'invalid ip address'
    with pytest.raises(ValueError):
        _inet_paton(setup_invalid_ip)
