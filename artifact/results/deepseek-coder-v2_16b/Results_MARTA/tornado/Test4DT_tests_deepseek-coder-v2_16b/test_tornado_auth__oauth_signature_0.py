
import pytest
from tornado.auth import _oauth_signature
from typing import Dict, Any, Optional
import urllib.parse
import hmac
import hashlib
import binascii

def test_valid_inputs():
    consumer_token = {'key': 'consumerKey', 'secret': 'consumerSecret'}
    parameters = {'param1': 'value1', 'param2': 'value2'}
    signature = _oauth_signature(consumer_token, 'GET', 'https://api.example.com/resource?param1=value1&param2=value2', parameters)
    assert isinstance(signature, bytes), "Signature should be a byte sequence"
    assert len(signature) > 0, "Signature should not be empty"

def test_edge_cases():
    consumer_token = None
    token = {}
    parameters = {}
    with pytest.raises(TypeError):
        _oauth_signature(consumer_token, 'POST', '', parameters)

def test_invalid_inputs():
    consumer_token = {}
    token = {'key': 'tokenKey'}
    parameters = {}
    with pytest.raises(KeyError):
        _oauth_signature(consumer_token, 'POST', 'https://api.example.com/resource', parameters)
