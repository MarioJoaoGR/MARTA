
import pytest
from unittest.mock import patch
from tornado.netutil import Resolver
from collections import deque
from typing import Any, Dict, Optional, Tuple, Callable
from tornado.simple_httpclient import SimpleAsyncHTTPClient as Client

@pytest.fixture
def default_client():
    return Client()

@pytest.fixture
def custom_resolver_client():
    resolver = Resolver()
    return Client(resolver=resolver, max_buffer_size=209715200)

@pytest.fixture
def hostname_mapping_client():
    resolver = Resolver()
    return Client(resolver=resolver, hostname_mapping={"localhost": "127.0.0.1"})

@pytest.fixture
def default_settings_with_headers():
    defaults = {
        "User-Agent": "MyCustomUserAgent/1.0",
        "Accept": "application/json"
    }
    return Client(defaults=defaults)

@pytest.fixture
def custom_header_sizes():
    return Client(max_header_size=8192, max_body_size=1048576)

def test_default_initialization(default_client):
    assert default_client.max_clients == 10