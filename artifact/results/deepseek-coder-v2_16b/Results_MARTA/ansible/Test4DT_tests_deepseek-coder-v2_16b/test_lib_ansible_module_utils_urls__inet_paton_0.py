
import pytest
import socket
import sys
from ansible.module_utils.urls import to_bytes

def _inet_paton(ipname):
    """Try to convert an IP address to packed binary form

    Supports IPv4 addresses on all platforms and IPv6 on platforms with IPv6
    support.
    """
    # inet_aton() also accepts strings like '1'
    # Divergence: We make sure we have native string type for all python versions
    try:
        b_ipname = to_bytes(ipname, errors='strict')
    except UnicodeError:
        raise ValueError("%s must be an all-ascii string." % repr(ipname))

    # Set ipname in native string format
    if sys.version_info < (3,):
        n_ipname = b_ipname
    else:
        n_ipname = ipname

    if n_ipname.count('.') == 3:
        try:
            return socket.inet_aton(n_ipname)
        # Divergence: OSError on late python3.  socket.error earlier.
        # Null bytes generate ValueError on python3(we want to raise
        # ValueError anyway), TypeError # earlier
        except (OSError, socket.error, TypeError):
            pass

    try:
        return socket.inet_pton(socket.AF_INET6, n_ipname)
    # Divergence: OSError on late python3.  socket.error earlier.
    # Null bytes generate ValueError on python3(we want to raise
    # ValueError anyway), TypeError # earlier
    except (OSError, socket.error, TypeError):
        # Divergence .format() to percent formatting for Python < 2.6
        raise ValueError("%s is neither an IPv4 nor an IP6 "
                         "address." % repr(ipname))
    except AttributeError:
        # AF_INET6 not available
        pass

    # Divergence .format() to percent formatting for Python < 2.6
    raise ValueError("%s is not an IPv4 address." % repr(ipname))

def test_valid_ipv4():
    ipname = '192.168.1.1'
    expected_output = b'\xc0\xa8\x01\x01'
    assert _inet_paton(ipname) == expected_output

def test_valid_ipv6():
    ipname = '::1'
    expected_output = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    assert _inet_paton(ipname) == expected_output

def test_invalid_input():
    ipname = 'invalid ip address'
    with pytest.raises(ValueError):
        _inet_paton(ipname)
