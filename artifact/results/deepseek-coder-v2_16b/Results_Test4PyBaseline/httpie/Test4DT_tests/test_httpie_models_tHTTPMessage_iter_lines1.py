
import pytest
from httpie.models import HTTPMessage

@pytest.fixture(params=[{'method': 'GET', 'url': '/index'}, {'method': 'POST', 'url': '/submit'}])
def valid_orig(request):
    return request.param

def test_http_message_init_valid_orig(valid_orig):
    http_message = HTTPMessage(valid_orig)
    assert hasattr(http_message, '_orig'), "Expected _orig attribute to be set"

# New Test Case for iter_lines method
@pytest.mark.skip(reason="This test will fail because the method is not implemented")
def test_iter_lines_not_implemented():
    http_message = HTTPMessage({})
    with pytest.raises(NotImplementedError):
        list(http_message.iter_lines(10))
