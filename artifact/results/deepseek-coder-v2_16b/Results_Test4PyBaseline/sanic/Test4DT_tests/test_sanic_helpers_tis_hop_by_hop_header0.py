# Module: sanic.helpers
import pytest
from sanic.helpers import is_hop_by_hop_header

# List of known Hop-By-Hop headers for testing purposes
_HOP_BY_HOP_HEADERS = {'connection', 'keep-alive', 'proxy-authenticate', 'proxy-authorization', 'te', 'trailer', 'transfer-encoding', 'upgrade'}

def test_is_hop_by_hop_header_known():
    assert is_hop_by_hop_header("Connection") == True
    assert is_hop_by_hop_header("keep-alive") == True  # Case insensitive check

def test_is_hop_by_hop_header_unknown():
    assert is_hop_by_hop_header("Content-Length") == False
    assert is_hop_by_hop_header("cache-control") == False  # Not in the list of Hop-By-Hop headers

def test_is_hop_by_hop_header_mixed_case():
    assert is_hop_by_hop_header("cOnNeCtIoN") == True  # Mixed case check

def test_is_hop_by_hop_header_conditional():
    if is_hop_by_hop_header("Keep-Alive"):
        assert True
    else:
        assert False
