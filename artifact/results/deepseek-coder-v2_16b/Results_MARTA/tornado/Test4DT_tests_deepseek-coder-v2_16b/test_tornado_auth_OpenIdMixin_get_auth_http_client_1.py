
import pytest
from tornado.auth import OpenIdMixin
from tornado import httpclient

class TestOpenIdMixin:
    def test_get_auth_http_client(self):
        class CustomOpenIdMixin(OpenIdMixin):
            pass
        
        custom_mixin = CustomOpenIdMixin()
        client = custom_mixin.get_auth_http_client()
        
        assert isinstance(client, httpclient.AsyncHTTPClient)
