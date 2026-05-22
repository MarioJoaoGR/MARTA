
import pytest
from unittest.mock import patch
from httpie.sessions import strip_port

def test_valid_input_without_port():
    hostname = 'example.com'
    assert strip_port(hostname) == 'example.com'
    
    hostname_with_port = 'example.com:8080'
    assert strip_port(hostname_with_port) == 'example.com'
    
    localhost_with_port = 'localhost:3000'
    assert strip_port(localhost_with_port) == 'localhost'
