
import pytest
from unittest.mock import patch
from httpie.sessions import strip_port

def test_valid_input_with_port():
    hostname = 'example.com:8080'
    assert strip_port(hostname) == 'example.com'
