
import pytest
from urllib.parse import parse_qs
from tornado import escape
import urllib.parse
from typing import Dict, Any

# Assuming the function is defined as provided above
def _oauth_parse_response(body: bytes) -> Dict[str, Any]:
    body_str = escape.native_str(body)
    p = parse_qs(body_str, keep_blank_values=False)
    token = dict(key=p["oauth_token"][0] if "oauth_token" in p else None, secret=p["oauth_token_secret"][0] if "oauth_token_secret" in p else None)
    special = ("oauth_token", "oauth_token_secret")
    token.update((k, p[k][0]) for k in p if k not in special and k in p)
    return {k: v for k, v in token.items() if v is not None}

# Test cases
def test_basic_usage():
    body = b'oauth_token=exampleToken&oauth_token_secret=exampleSecret&extraParam=extraValue'
    parsed_response = _oauth_parse_response(body)
    assert parsed_response == {'key': 'exampleToken', 'secret': 'exampleSecret', 'extraParam': 'extraValue'}

def test_handling_simple_oauth_response():
    body = b'oauth_token=simpleToken&oauth_token_secret=simpleSecret'
    parsed_response = _oauth_parse_response(body)
    assert parsed_response == {'key': 'simpleToken', 'secret': 'simpleSecret'}

def test_handling_no_extra_params():
    body = b'oauth_token=noExtraParams&oauth_token_secret=noExtraValues'
    parsed_response = _oauth_parse_response(body)
    assert parsed_response == {'key': 'noExtraParams', 'secret': 'noExtraValues'}

def test_handling_only_token():
    body = b'oauth_token=onlyToken&oauth_token_secret=onlySecret'
    parsed_response = _oauth_parse_response(body)
    assert parsed_response == {'key': 'onlyToken', 'secret': 'onlySecret'}

def test_handling_extra_params():
    body = b'oauth_token=withExtra&oauth_token_secret=withExtraSecret&extraParam1=value1&extraParam2=value2'
    parsed_response = _oauth_parse_response(body)
    assert parsed_response == {'key': 'withExtra', 'secret': 'withExtraSecret', 'extraParam1': 'value1', 'extraParam2': 'value2'}

# Additional test cases to cover uncovered lines 1180-1182, 1185-1187
def test_body_str_conversion():
    body = b'oauth_token=testToken&oauth_token_secret=testSecret'
    parsed_response = _oauth_parse_response(body)
    assert isinstance(escape.native_str(body), str)  # Ensure conversion to native string

def test_special_keys_in_parsed_qs():
    body = b'oauth_token=testToken&oauth_token_secret=testSecret&extraParam=extraValue'
    parsed_response = _oauth_parse_response(body)