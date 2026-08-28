
import pytest
from tornado import httpclient
from tornado.httpclient import HTTPError



def test_valid_input():
    with pytest.raises(ValueError):
        try:
            response = httpclient.HTTPClient().fetch("invalidscheme://example.com/")
        except ValueError as e:
            assert str(e) == "Unsupported url scheme: invalidscheme://example.com/"
            raise