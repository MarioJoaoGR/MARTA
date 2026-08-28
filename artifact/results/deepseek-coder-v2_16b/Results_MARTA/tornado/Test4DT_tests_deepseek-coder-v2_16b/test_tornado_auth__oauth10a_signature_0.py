
import pytest
import urllib.parse
import hmac
import hashlib
import binascii
from typing import Dict, Any, Optional

def _oauth_escape(value: str) -> str:
    """Helper function to escape OAuth parameters."""
    return urllib.parse.quote(value, safe="~")

def _oauth10a_signature(
    consumer_token: Dict[str, Any],
    method: str,
    url: str,
    parameters: Dict[str, Any] = {},
    token: Optional[Dict[str, Any]] = None,
) -> bytes:
    """Calculates the HMAC-SHA1 OAuth 1.0a signature for the given request."""
    parts = urllib.parse.urlparse(url)
    scheme, netloc, path = parts[:3]
    normalized_url = scheme.lower() + "://" + netloc.lower() + path

    base_elems = []
    base_elems.append(method.upper())
    base_elems.append(normalized_url)
    base_elems.append(
        "&".join(
            "%s=%s" % (k, _oauth_escape(str(v))) for k, v in sorted(parameters.items())
        )
    )

    base_string = "&".join(_oauth_escape(e) for e in base_elems)
    key_elems = [urllib.parse.quote(consumer_token["secret"], safe="~")]
    key_elems.append(
        urllib.parse.quote(token["secret"] if token else "", safe="~")
    )
    key = "&".join(key_elems)

    hash = hmac.new(bytes(key, "latin1"), bytes(base_string, "latin1"), hashlib.sha1)
    return binascii.b2a_base64(hash.digest())[:-1]

# Test cases for valid inputs
def test_valid_inputs():
    consumer_token = {'key': 'consumerKey', 'secret': 'consumerSecret'}
    parameters = {'param1': 'value1', 'param2': 'value2'}
    signature = _oauth10a_signature(consumer_token, 'GET', 'https://api.example.com/resource?param=value')
    assert isinstance(signature, bytes)
    assert len(signature) > 0

# Test cases for edge cases
def test_edge_cases():
    consumer_token = {}
    method = ''
    url = ''
    parameters = {}
    with pytest.raises(KeyError):
        _oauth10a_signature(consumer_token, method, url, parameters)

# Test cases for invalid inputs
def test_invalid_inputs():
    consumer_token = None
    method = 'GET'
    url = 'https://api.example.com/resource?param=value'
    parameters = {'invalid': 'data'}
    with pytest.raises(TypeError):
        _oauth10a_signature(consumer_token, method, url, parameters)
