
import pytest
from tornado import httpclient, web
from unittest.mock import patch

class TestOpenIdMixin:
    @pytest.mark.asyncio
    async def test_get_auth_http_client(self):
        class MyHandler(web.RequestHandler, OpenIdMixin):
            pass
        
        handler = MyHandler()
        with patch('tornado.httpclient.AsyncHTTPClient') as mock_client:
            client = handler.get_auth_http_client()
            assert isinstance(client, httpclient.AsyncHTTPClient)
