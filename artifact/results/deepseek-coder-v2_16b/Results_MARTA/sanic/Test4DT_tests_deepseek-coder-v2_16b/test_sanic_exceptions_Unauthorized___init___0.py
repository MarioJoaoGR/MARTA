
import pytest
from sanic.exceptions import Unauthorized

# Test for Basic authentication scheme
def test_valid_input_basic_scheme():
    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized("Authentication required.", scheme="Basic", realm="Restricted Area")
    
    assert str(excinfo.value) == "Authentication required."
    assert excinfo.value.headers["WWW-Authenticate"] == "Basic realm=\"Restricted Area\""

# Test for Digest authentication scheme
def test_valid_input_digest_scheme():
    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized("Authentication required.", scheme="Digest", realm="Example Realm", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    
    assert str(excinfo.value) == "Authentication required."
    assert excinfo.value.headers["WWW-Authenticate"] == "Digest realm=\"Example Realm\", qop=\"auth, auth-int\", algorithm=\"MD5\", nonce=\"abcdef\", opaque=\"zyxwvu\""

# Test for Bearer authentication scheme
def test_valid_input_bearer_scheme():
    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized("Authentication required.", scheme="Bearer", realm="Restricted Area")
    
    assert str(excinfo.value) == "Authentication required."
    assert excinfo.value.headers["WWW-Authenticate"] == "Bearer realm=\"Restricted Area\""
