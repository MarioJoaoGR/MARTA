
import pytest
from unittest.mock import patch
from sanic.headers import parse_host


def test_valid_host_with_port():
    expected_hostname = "example.com"
    expected_port = 8080
    with patch('sanic.headers.parse_host', return_value=(expected_hostname, expected_port)):
        host = f"{expected_hostname}:{expected_port}"
        assert parse_host(host) == (expected_hostname, expected_port)

def test_valid_host_without_port():
    expected_hostname = "example.com"
    with patch('sanic.headers.parse_host', return_value=(expected_hostname, None)):
        host = expected_hostname
        assert parse_host(host) == (expected_hostname, None)
