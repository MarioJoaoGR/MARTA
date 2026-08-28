
import pytest
from tornado import escape, httpclient
import urllib.parse
from typing import Dict, Any

def _oauth_parse_response(body: bytes) -> Dict[str, Any]:
    body_str = escape.native_str(body)
    p = urllib.parse.parse_qs(body_str, keep_blank_values=False)
    token = dict(key=p["oauth_token"][0] if "oauth_token" in p else None, secret=p["oauth_token_secret"][0] if "oauth_token_secret" in p else None)
    special = ("oauth_token", "oauth_token_secret")
    token.update((k, p[k][0]) for k in p if k not in special and k in p)
    return token


def test_basic_response():
    body = b"oauth_token=exampleToken&oauth_token_secret=exampleSecret&extra_param=extraValue"
    parsed_response = _oauth_parse_response(body)
    expected_response = {'key': 'exampleToken', 'secret': 'exampleSecret', 'extra_param': 'extraValue'}
    assert parsed_response == expected_response

def test_no_additional_params():
    body = b"oauth_token=anotherToken&oauth_token_secret=anotherSecret"
    parsed_response = _oauth_parse_response(body)
    expected_response = {'key': 'anotherToken', 'secret': 'anotherSecret'}
    assert parsed_response == expected_response
