
import pytest
from tornado import httpclient, web
from tornado.auth import OAuthMixin

class TestOAuthMixin(object):
    
    def setup_method(self, method):
        self.mixin = OAuthMixin()

    @pytest.mark.asyncio
    async def test_get_auth_http_client(self):
        client = self.mixin.get_auth_http_client()
        assert isinstance(client, httpclient.AsyncHTTPClient)

    @pytest.mark.asyncio
    async def test_oauth_consumer_token(self):
        with pytest.raises(NotImplementedError):
            self.mixin._oauth_consumer_token()

    @pytest.mark.asyncio
    async def test_oauth_request_token_url(self):
        with pytest.raises(NotImplementedError):
            self.mixin._oauth_request_token_url()

    @pytest.mark.asyncio
    async def test_oauth_access_token_url(self):
        with pytest.raises(NotImplementedError):
            self.mixin._oauth_access_token_url()
