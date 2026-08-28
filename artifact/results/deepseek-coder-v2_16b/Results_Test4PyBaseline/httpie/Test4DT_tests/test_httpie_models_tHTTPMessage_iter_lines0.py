
import pytest
from httpie.models import HTTPMessage

@pytest.fixture(params=[{'method': 'GET', 'url': '/index'}, {'method': 'POST', 'url': '/submit'}])
def valid_orig(request):
    return request.param

def test_http_message_init_valid_orig(valid_orig):
    http_message = HTTPMessage(valid_orig)
    assert hasattr(http_message, '_orig'), "Expected _orig attribute to be set"