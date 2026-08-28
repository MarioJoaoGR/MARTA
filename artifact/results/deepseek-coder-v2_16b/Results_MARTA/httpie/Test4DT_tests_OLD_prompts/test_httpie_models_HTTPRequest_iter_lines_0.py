
import pytest
from httpie.models import HTTPRequest

def test_valid_input():
    with pytest.raises(TypeError):
        http_request = HTTPRequest()

def test_edge_case():
    with pytest.raises(TypeError):
        http_request = HTTPRequest()

def test_invalid_input():
    with pytest.raises(TypeError):
        http_request = HTTPRequest()
