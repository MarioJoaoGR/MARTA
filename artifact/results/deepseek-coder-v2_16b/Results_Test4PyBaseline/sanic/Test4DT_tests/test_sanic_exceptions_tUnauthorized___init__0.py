# Module: sanic.exceptions
import pytest
from sanic.exceptions import Unauthorized

# Test cases for Unauthorized exception with different authentication schemes

def test_basic_authentication():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert str(e) == "Auth required."
        assert e.headers["WWW-Authenticate"] == 'Basic realm="Restricted Area"'

def test_digest_authentication():
    try:
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except Unauthorized as e:
        assert str(e) == "Auth required."
        assert e.headers["WWW-Authenticate"] == 'Digest realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu"'

def test_bearer_token_authentication():
    try:
        raise Unauthorized("Auth required.", scheme="Bearer")
    except Unauthorized as e:
        assert str(e) == "Auth required."
        assert e.headers["WWW-Authenticate"] == 'Bearer'

def test_bearer_token_with_realm():
    try:
        raise Unauthorized("Auth required.", scheme="Bearer", realm="Restricted Area")
    except Unauthorized as e:
        assert str(e) == "Auth required."
        assert e.headers["WWW-Authenticate"] == 'Bearer realm="Restricted Area"'

if __name__ == "__main__":
    pytest.main()
